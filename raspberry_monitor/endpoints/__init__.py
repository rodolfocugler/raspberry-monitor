import json

from flask_restx import Api

from raspberry_monitor.endpoints.metric import api as ns_metric
from raspberry_monitor.endpoints.commands import api as ns_commands


def get_authorizations():
    from raspberry_monitor import config
    conf = config.Config()
    if conf.OIDC_ENABLED:
        with open(conf.OIDC_CLIENT_SECRETS) as f:
            data = json.load(f)
        return {
            "auth": {
                "type": "oauth2",
                "bearerFormat": "JWT",
                "tokenUrl": data["web"]["token_uri"],
                "authorizationUrl": data["web"]["auth_uri"],
                "flow": "password"
            }
        }
    elif conf.BASIC_AUTH_FORCE:
        return {
            "auth": {
                "type": "basic"
            }
        }


api = Api(
    title="Raspberry-Monitor",
    version="1.0",
    description="Monitor Raspberry Pi 4.0 - (Ubuntu 64bits)",
    authorizations=get_authorizations(), security="auth"
)

api.add_namespace(ns_metric, path="/api")
api.add_namespace(ns_commands, path="/api")
