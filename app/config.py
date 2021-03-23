import os
import sys

EXEC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = os.path.join(EXEC_DIR, 'uploads')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'postgresql://yourusername:yourpassword@localhost/databasename'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Create the upload folder if its deleted
    if os.path.isdir(UPLOAD_FOLDER) is False:
        os.mkdir(UPLOAD_FOLDER)


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    DEBUG = False
