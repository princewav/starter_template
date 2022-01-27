from .config import current_config as conf


def main():
    print(f"{conf.DATA_PATH} -> Exists: {conf.DATA_PATH.exists()}")


if __name__ == "__main__":
    main()
