"""
  Defining the configurations
"""  
class Config(object):
    """
       Defining the default environment
    """  
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """
      Defining the development environment
    """   
    DEBUG = True
    TESTING = True
    ENV = "development"
