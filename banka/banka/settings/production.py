from .base import *
from ..db import DB


ENV = 'production'

DATABASES = DB.db_config(ENV)
