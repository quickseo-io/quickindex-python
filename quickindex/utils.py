import json


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_urls_to_file(urls, file_path):
    with open(file_path, 'w') as file:
        json.dump(urls, file, indent=4)
