class Config:

    TESTING = False

class Development(Config):

    DEBUG = True
    ENV = 'development'

class Production(Config):

    DEBUG = False
    ENV = 'production'

APP_CONFIG = {
    'development': Development,
    'production': Production,
}
