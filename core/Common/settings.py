from collections.abc import Collection
from os import curdir
from pydantic_settings import BaseSettings
from distutils.util import strtobool
import environ
import logging
import logging.config
import yaml
import pathlib

###########################enivroment configuration#############################

BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env('DEBUG', cast=strtobool, default=False)
    uri : str = env.str('URI')
    db : str = env.str('DB')
    collection : str = env.str('COLLECTION')
    user : str = env.str('USER')
    password : str = env.str('PASS')

settings = Settings()
print(settings.debug, BASE_DIR)
print("--------------DB SETTING--------------")
print(f"uri:{settings.uri}")
print(f"db:{settings.db}")
print(f"collection:{settings.collection}")
print(f"user:{settings.user}")
print(f"pass:{settings.password}")
print("--------------------------------------")

############################logging configuration###############################


current_directory = pathlib.Path(__file__).resolve().parent.parent
config_file_path = current_directory / 'logger.yaml'

with config_file_path.open('r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
logger = logging.getLogger('debugging')
logger.debug('debug mode activated')
