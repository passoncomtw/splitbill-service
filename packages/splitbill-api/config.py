from dotenv import load_dotenv
import os

load_dotenv()


def convert_bool_str(value):
    return value == "True"

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = convert_bool_str(os.environ.get("TESTING"))
    DEBUG = convert_bool_str(os.environ.get("DEBUG"))
    SQLALCHEMY_ECHO = convert_bool_str(os.environ.get("SQLALCHEMY_ECHO"))
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.environ.get('DB_URL')}/{os.environ.get('DB_NAME')}"
    )


class Test_Config(Config):
    TESTING = True