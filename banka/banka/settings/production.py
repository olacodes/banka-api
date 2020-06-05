from .base import *
from decouple import config
from ..db import DB


ENV = 'production'

DATABASES = DB.db_config(ENV)
