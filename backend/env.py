import pathlib
from functools import lru_cache
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_FILES = [
    ".env",
    ".env.local",
]

@lru_cache
def get_config():
    for env_file in ENV_FILES:
        env_base_path = BASE_DIR / env_file
        if env_base_path.exists():
            return Config(RepositoryEnv(str(env_base_path)))
    from decouple import config as _config
    return _config

config = get_config()