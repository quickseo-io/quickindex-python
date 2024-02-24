import json

import httplib2
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def index_url(url, credentials_json):
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
        print(f"URL: {url} indexed.")
        return True

    print(f"URL: {url} could not be indexed.")
    print(f"Response: {response}")
    return False
