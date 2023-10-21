from os import curdir
from pydantic_settings import BaseSettings
from distutils.util import strtobool
import environ
import logging
import logging.config
import yaml
import pathlib


BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env('DEBUG', cast=strtobool, default=False)

settings = Settings()
print(settings.debug, BASE_DIR)

current_directory = pathlib.Path(__file__).resolve().parent.parent
config_file_path = current_directory / 'logger.yaml'

with config_file_path.open('r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
logger = logging.getLogger('debugging')
logger.debug('debug mode activated')
