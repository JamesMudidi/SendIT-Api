class BaseConfig:
    DEBUG = False
    TEST = False
    
class ProductionConfig(BaseConfig):
    TEST = False
    DEBUG = False    
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TEST = True

config = {
    'Testing': TestingConfig,
    'development': ProductionConfig,
    'production': ProductionConfig
}
