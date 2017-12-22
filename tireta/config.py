from pathlib import Path

here = Path(__file__).resolve().parent


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{here}/tireta.db'


config = {
    'test': TestConfig,
    'dev': DevConfig,

    'default': DevConfig,
}
