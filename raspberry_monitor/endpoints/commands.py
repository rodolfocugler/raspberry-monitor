import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource, abort, reqparse

from raspberry_monitor import config, oidc
from raspberry_monitor.services import power_mode

api = Namespace("commands")

conf = config.Config()

_post_parser = reqparse.RequestParser()
_post_parser.add_argument("command_id", type=str, required=True, help="Command Id", default="restart")


@api.route("/commands")
class Command(Resource):

    @api.doc("/",
             responses={
                 HTTPStatus.UNAUTHORIZED: "Request unauthorized",
                 HTTPStatus.OK: "Command successful executed"
             },
             security="auth")
    @api.expect(_post_parser)
    @oidc.accept_token(require_token=conf.OIDC_ENABLED)
    @oidc.require_keycloak_role(require_token=conf.OIDC_ENABLED, client=conf.OIDC_CLIENT,
                                roles=["admin", "uma_protection"],
                                all_roles_required=False)
    def post(self):
        args = _post_parser.parse_args()
        command_id = args["command_id"]

        logging.debug(f"Executing {command_id}")
        if command_id == "restart":
            power_mode.restart()
        elif command_id == "shutdown":
            power_mode.shutdown()
        else:
            abort(400, "Command Id is invalid")
