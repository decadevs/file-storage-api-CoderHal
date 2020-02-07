import dj_database_url
from decouple import config

def db_config(DEBUG, url):
    if DEBUG == True:
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'filestore',
                'HOST': 'localhost',
                'PORT': 27017
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'HOST': url
            }
        }
    return DATABASES
