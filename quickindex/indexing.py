import json

import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from quickindex.utils import APP_LOGGER

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def index_url(url, credentials_json, index):
    content = {
        'url': url,
        'type': 'URL_UPDATED'
    }

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_json, scopes=SCOPES
    )
    http = credentials.authorize(httplib2.Http())

    response, content = http.request(ENDPOINT, method="POST", body=json.dumps(content))

    if response.status == 200:
        APP_LOGGER.info(f"[{index}]URL: {url} indexed.")
        return True

    if response.status == 429:
        raise Exception("Rate limit reached. Please wait and try again.")

    APP_LOGGER.warning(f"[{index}]URL: {url} could not be indexed.")
    APP_LOGGER.info(f"Response status: {response.status}")

    raise Exception(f"Response status: {response.status}")
