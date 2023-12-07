import os


class Config:
    APP_NAME = os.getenv("FLASK_APP")
    BACKUP_PATH = os.getenv("BACKUP_PATH", None)