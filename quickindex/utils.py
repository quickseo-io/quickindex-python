import json
import logging
import logging.config


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_urls_to_file(urls, file_path):
    with open(file_path, 'w') as file:
        json.dump(urls, file, indent=4)


def create_logger() -> logging.Logger:
    # create logger
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("google_quickindex")

    return logger


APP_LOGGER = create_logger()
