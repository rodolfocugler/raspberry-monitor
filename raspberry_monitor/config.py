import os


class Config:
    APP_NAME = os.getenv("FLASK_APP")

    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME", "admin")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "123456")
    BASIC_AUTH_FORCE = os.getenv("BASIC_AUTH_FORCE", "True") == "True"

    OIDC_ENABLED = os.getenv("OIDC_ENABLED", "False") == "True"
    OIDC_OPENID_REALM = os.getenv("OIDC_OPENID_REALM", "raspberry-pi")
    OIDC_CLIENT = os.getenv("OIDC_CLIENT", "raspberry-monitor")
    OIDC_INTROSPECTION_AUTH_METHOD = "client_secret_post"
    OIDC_TOKEN_TYPE_HINT = "access_token"
    OIDC_CLIENT_SECRETS = os.getenv("BASE_PATH") + os.getenv("OIDC_CLIENT_SECRETS", "/client_secrets.json")
