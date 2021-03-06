__author__ = 'snwiem'

DEBUG = True
TESTING = True
SECRET_KEY = "MySecretKey!"
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

ALBUM_ROOT = "./albums"
IMAGE_EXTS = [ "png", "gif", "jpg", "jpeg", "bmp" ]
THUMB_ROOT = "./cache/thumbs"
THUMB_DIMS = (400, 300)

# WTF
WTF_CSRF_ENABLED = True
#WTF_CSRF_SECRET_KEY = Same as SECRET_KEY
WTF_CSRF_TIME_LIMIT = 3600
WTF_CSRF_SSL_STRICT = True