"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
"""


class Config:
    ENV: str = 'development'
    DEBUG: bool = True
    TESTING: bool = True


class ProdConfig(Config):
    ENV: str = 'production'
    DEBUG: bool = False
    TESTING: bool = False


class DevelopmentConfig(Config):
    ...


class TestingConfig(Config):
    ...
