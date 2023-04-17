import logging
import os
from dotenv import load_dotenv

DEBUG = False
load_dotenv()
logging.basicConfig(filename="error.log", level=logging.DEBUG,
                    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")
logging.getLogger('flask_cors').level = logging.DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_TYPE = "filesystem"
if os.environ.get("DEBUG_ENV") == "dev":
    DEBUG = True
CORS_METHODS = ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"]
CORS_HEADERS = ["Content-Type", "Authorization", "Access-Control-Allow-Credentials"]
CORS_SUPPORTS_CREDENTIALS = True
CORS_ORIGINS = ["*"]
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE = os.environ.get('DATABASE')
