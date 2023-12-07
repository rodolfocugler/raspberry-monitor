import json

from flask_restx import Api

from raspberry_monitor.endpoints.metric import api as ns_metric


api = Api(
    title="Raspberry-Monitor",
    version="1.0",
    description="Monitor Raspberry Pi 4.0 - (Ubuntu 64bits)"
)

api.add_namespace(ns_metric, path="/api")
