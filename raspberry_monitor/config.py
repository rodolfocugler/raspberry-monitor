import os


class Config:
    APP_NAME = os.getenv("FLASK_APP")
    BACKUP_PATH = os.getenv("BACKUP_PATH", None)
    SSH_LOG_PATH = os.getenv("SSH_LOG_PATH", None)
