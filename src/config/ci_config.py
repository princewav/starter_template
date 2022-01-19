from .dev_config import DevConfig


class CIConfig(DevConfig):
    ENV = "ci"
