import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource

from raspberry_monitor.services import metric_read

api = Namespace("metrics")


@api.route("/metrics")
class Metric(Resource):

    @api.doc("/",
             responses={
                 HTTPStatus.OK: "Metrics"
             })
    def get(self):
        logging.debug(f"get metrics")
        metrics = metric_read.get()
        logging.info(f"return {metrics}")
        return metrics
