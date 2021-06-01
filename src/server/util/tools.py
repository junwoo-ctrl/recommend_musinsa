import os
from os import path
from dataclasses import dataclass


base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


class EnvTool:
    ENV_NAME_KEY: str = 'ENV'
    ENV_DEV: str = 'DEV'
    ENV_PROD: str = 'PROD'

    @staticmethod
    def get_env():
        env = os.environ.get(EnvTool.ENV_NAME_KEY, EnvTool.ENV_DEV).lower()
        return env


@dataclass
class BasicConfig:
    BASE_PATH: str = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class DevConfig(BasicConfig):
    # To be migrate third-party secret store
    PROJ_RELOAD: bool = True
    user: str = 'musinsa'
    password: str = 'xhakxhsoaql1!'
    host: str = 'localhost'
    database: str = 'dev'


@dataclass
class ProdConfig(BasicConfig):
    # To be migrate third-party secret store
    PROJ_RELOAD: bool = False
    user: str = 'musinsa'
    password: str = 'xhakxhsoaql1!'
    host: str = 'localhost'
    database: str = 'prod'


class Config:
    
    @staticmethod
    def get_config():
        config = dict(prod=ProdConfig(), dev=DevConfig())
        env = EnvTool.get_env()
        return config.get(env)
