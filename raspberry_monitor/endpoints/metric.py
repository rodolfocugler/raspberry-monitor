import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource

from raspberry_monitor import config, oidc
from raspberry_monitor.metrics import metric_read

api = Namespace("metrics")

conf = config.Config()


@api.route("/metrics")
class Metric(Resource):

    @api.doc("/",
             responses={
                 HTTPStatus.UNAUTHORIZED: "Request unauthorized",
                 HTTPStatus.OK: "Metrics"
             },
             security="auth")
    @oidc.accept_token(require_token=conf.OIDC_ENABLED)
    @oidc.require_keycloak_role(require_token=conf.OIDC_ENABLED, client=conf.OIDC_CLIENT,
                                roles=["admin", "uma_protection"],
                                all_roles_required=False)
    def get(self):
        logging.debug(f"get metrics")
        metrics = metric_read.get()
        logging.info(f"return {metrics}")
        return metrics
