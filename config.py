class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='ASDSR4RWEfasdfawer~!'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dev:bountyhunter@db_server/dev?charset=utf8mb4'
    SQLALCHEMY_POOL_RECYCLE = 300
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/prd'

config = {
    "dev": DevelopmentConfig(),
    "test": TestConfig(),
    "prd": ProductionConfig(),
    "default": DevelopmentConfig()
}
