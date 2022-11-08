from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True

    DB_USER: str = "root"
    DB_PASSWORD: str = "f8hYoMq2B3H0a4AxAvzU"
    DB_HOST: str = "localhost"
    DB_SCHEMA: str = "WebForSimpleEnjoy"
    DB_CHARSET: str = "utf8mb4"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    config = dict(prod=ProdConfig, local=LocalConfig)
    return config[environ.get('API_ENV', 'local')]()
