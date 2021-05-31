from dataclasses import asdict

from src.app.util.tools import EnvTool
from src.app.util.tools import Config


def test_env_tool():
    
    pjt_env_name_key = 'ENV'
    assert EnvTool.ENV_NAME_KEY == pjt_env_name_key

    pjt_develop_env_name, pjt_product_env_name = 'DEV', 'PROD'
    assert EnvTool.ENV_DEV = pjt_develop_env_name
    assert EnvTool.ENV_PROD = pjt_product_env_name
    
    current_env_name = EnvTool.get_env()
    assert current_env_name in ['DEV', 'PROD']


def test_config():
    config = Config.get_config()
    
    basic_config_properties = set('BASE_PATH', 'DB_POOL_RECYCLE', 'DB_ECHO')
    config_properties = set('PROJ_RELOAD', 'user', 'password', 'host', 'database')

    config_dict = asdict(config)
    keyset = set(config_dict.keys())

    assert basic_config_properties.issubset(keyset)
    assert config_properties.issubset(keysets)
