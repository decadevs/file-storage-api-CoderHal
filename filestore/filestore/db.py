import dj_database_url
from decouple import config


# class DB:
#     @classmethod
#     def db_config(cls, debug):
#         return cls.development() if debug else cls.production()

#     @classmethod
#     def production():
#         return{
#              'default': {
#                 **dj_database_url.parse(config("DATABASE_URL", cast=str, default={}), conn_max_age=600),
#                 'ENGINE': 'django.db.backends.djongo'
#             }
#         }

#     @classmethod
#     def development():
#         return {
#             'default': {
#                 'ENGINE': 'djongo',
#                 'NAME': 'filestore',
#                 'HOST': 'localhost:27017',
#                 'USERNAME': 'hal',
#                 'PASSWORD': 'curly', 
#             }
#         }

# DEBUG = config('DEBUG', default=True, cast=bool)

def db_config():
    if DEBUG == True:
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'filestore',
                'HOST': 'localhost:27017',
                'USERNAME': 'hal',
                'PASSWORD': 'curly', 
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
