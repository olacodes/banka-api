from .base import *
from decouple import config
from ..db import DB


ENV = 'development'

DATABASES = DB.db_config(ENV)

