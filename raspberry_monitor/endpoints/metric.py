import flask
import logging
from flask_restx import Namespace, Resource

from raspberry_monitor import config
from raspberry_monitor.services import metric_read

api = Namespace("metrics")

conf = config.Config()


@api.route("/metrics")
class AllMetrics(Resource):

    def get(self):
        logging.debug("get metrics")
        metrics = metric_read.get()
        logging.info(f"return {metrics}")
        return metrics


@api.route("/metrics/resource/<string:resource>")
class Metric(Resource):

    def get(self, resource):
        logging.debug(f"get metrics: {resource}")

        metric = None
        if resource == "memory":
            metric = metric_read.get_memory()
        elif resource == "disk":
            metric = metric_read.get_disk()
        elif resource == "temperature":
            metric = metric_read.get_temperature()
        elif resource == "cpu":
            metric = metric_read.get_cpu()
        elif resource == "network":
            metric = metric_read.get_network()
        elif conf.BACKUP_PATH is not None and resource == "backups":
            metric = metric_read.get_backups()
        elif conf.SSH_LOG_PATH is not None and resource == "ssh_accesses":
            metric = metric_read.get_last_ssh_accesses()
        else:
            flask.abort(400, "Resource is invalid")

        logging.info(f"return {metric}")
        return metric
