class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='ASDSR4RWEfasdfawer~!'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dev:bountyhunter@127.0.0.1/dev'

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
