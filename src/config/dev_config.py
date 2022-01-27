import logging
from pathlib import Path


class DevConfig:
    ENV: str = "dev"

    ROOT_PATH: Path = Path(__file__).parent.parent
    DATA_PATH: Path = ROOT_PATH / "data"
    PROJECT_NAME: str = ROOT_PATH.parent.name
    LOG_LOCATION: str = f"var/log/{PROJECT_NAME}.log"
    LOG_LEVEL: int = logging.INFO
    LOG_FORMAT: str = (
        "[%(asctime)s | %(module)s:%(lineno)d | %(levelname)s] %(message)s"
    )
