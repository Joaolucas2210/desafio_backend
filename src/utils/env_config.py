from dynaconf import Dynaconf
from termcolor import cprint

settings = Dynaconf(load_dotenv=True)

class EnvConfig:
    @staticmethod
    def get(key, default=None):
      try:
        return settings.get(key, default)
      except Exception as e:
        cprint(e, 'red')
        raise e

