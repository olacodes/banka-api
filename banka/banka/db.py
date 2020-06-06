import os

import dj_database_url
from decouple import config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DB:
    @classmethod
    def db_config(cls, env):
        if env == 'development':
            return cls.development()
        elif env == 'testing':
            return cls.testing()
        else:
            return cls.production()

    @classmethod
    def production(cls):
        return {
            'default': {
                **dj_database_url.parse(config('DATABASE_URL')),
                'ENGINE': 'django.db.backends.postgresql'
            }
        }
    
    @classmethod
    def testing(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'bankadb',
                'HOST': 'db',
                'USER': config('DBUSER'),
                'PASSWORD': config('DBPASSWD'),
            }
        }
