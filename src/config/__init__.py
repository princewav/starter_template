from typing import Type

from .ci_config import CIConfig
from .dev_config import DevConfig
from .prod_config import ProdConfig

config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "ci": CIConfig,
}


def load_current_config() -> Type[DevConfig]:
    import dotenv
    import os

    dotenv.load_dotenv()
    env = os.getenv("ENV", "")

    return config.get(env, DevConfig)


current_config = load_current_config()
