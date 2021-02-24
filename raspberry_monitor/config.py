import os


class Config:
    APP_NAME = os.getenv("FLASK_APP")

    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME", "admin")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "123456")
    BASIC_AUTH_FORCE = True
