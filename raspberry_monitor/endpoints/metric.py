import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource

api = Namespace("metrics")


@api.route("/metrics")
class Metric(Resource):

    @api.doc("/",
             responses={
                 HTTPStatus.UNAUTHORIZED: "Request unauthorized",
                 HTTPStatus.OK: "Metrics"
             })
    def get(self):
        logging.info(f"get metrics")
        return ""
