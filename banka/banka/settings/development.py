from .base import *
from ..db import DB


ENV = 'development'

DATABASES = DB.db_config(ENV)

