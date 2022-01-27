from . import DevConfig


class ProdConfig(DevConfig):
    ENV = "prod"
