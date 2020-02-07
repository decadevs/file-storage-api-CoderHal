import dj_database_url
from decouple import config

def db_config(DEBUG, url):
    if DEBUG == True:
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'filestore',
                'HOST': 'localhost:27017'
            }
        }
    else:
        DATABASES = {
            'default': {
                **dj_database_url.parse(config("MONGODB_URI", cast=str, default={}), conn_max_age=600),
                'ENGINE': 'django.db.backends.djongo'
            }
        }
    return config
