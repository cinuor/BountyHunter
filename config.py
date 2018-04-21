class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/dev'

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
