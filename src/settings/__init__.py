from src.settings.base import environment

if environment == "development":
    from src.settings.dev import *
elif environment == "test":
    from src.settings.test import *
elif environment == "production":
    from src.settings.pro import *

CONFIG_CLASS = Settings

