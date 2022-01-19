import logging

from .base_config import Config


class DevConfig(Config):
    ENV: str = "dev"

    ROOT_LOCATION: str = "lite_server"
    LOG_LOCATION: str = "var/log/lite_server.log"
    LOG_LEVEL: int = logging.INFO
    LOG_FORMAT: str = (
        "[%(asctime)s | %(module)s:%(lineno)d | %(levelname)s] %(message)s"
    )

