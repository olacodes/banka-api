from .base import *
from ..db import DB


ENV = 'testing'

DATABASES = DB.db_config(ENV)
