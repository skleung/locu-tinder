import os

CSRF_ENABLED = True # activates CSRF prevention
SECRET_KEY = 'you-will-never-guess' # secret crytographic token used to validate a form

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

