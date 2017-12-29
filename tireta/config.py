from pathlib import Path

here = Path(__file__).resolve().parent


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):

    # for tests, database is in-memory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevConfig(BaseConfig):

    # for dev, use a file
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{here}/tireta.db'


config = {
    'test': TestConfig,
    'dev': DevConfig,

    'default': DevConfig,
}
