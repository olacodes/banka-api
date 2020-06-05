from .base import *
from decouple import config
from ..db import DB


ENV = 'testing'

DATABASES = DB.db_config(ENV)
