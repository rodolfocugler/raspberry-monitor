import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource, abort

from raspberry_monitor import config, oidc
from raspberry_monitor.services import power_mode

api = Namespace("commands")

conf = config.Config()


@api.route("/commands")
class Command(Resource):

    @api.doc("/",
             params={"command_id": "Command id"},
             responses={
                 HTTPStatus.UNAUTHORIZED: "Request unauthorized",
                 HTTPStatus.OK: "Command successful executed"
             },
             security="auth")
    @oidc.accept_token(require_token=conf.OIDC_ENABLED)
    @oidc.require_keycloak_role(require_token=conf.OIDC_ENABLED, client=conf.OIDC_CLIENT,
                                roles=["admin", "uma_protection"],
                                all_roles_required=False)
    def post(self, command_id):
        logging.debug(f"Executing {command_id}")
        if command_id == "restart":
            power_mode.restart()
        elif command_id == "shutdown":
            power_mode.shutdown()
        else:
            abort(400, "Command Id is invalid")
