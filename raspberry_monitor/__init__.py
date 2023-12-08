import logging
import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=os.urandom(16))

    from raspberry_monitor import config
    conf = config.Config()
    app.config.from_object(conf)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from raspberry_monitor.endpoints import api
    api.init_app(app)
    configure_logging()

    CORS(app, resources={r"*": {"origins": ["*"]}})

    return app


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s %(pathname)s:%(lineno)d - %(levelname)s - %(message)s",
                                  datefmt="%d-%b-%y %H:%M:%S")
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
