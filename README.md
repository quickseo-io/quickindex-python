# A Python script to quickly index your pages in Google Search

Made by [QuickIndex](https://quickindex.co) — A service to automatically index 1000s of pages in Google Search.

## Usage

1. Install the required packages using the following command:

```shell
pip install -r requirements.txt
```

2. Create a Project in the [Google Cloud Console](https://console.cloud.google.com/)


3. Create service account in Google
   Cloud: https://developers.google.com/search/apis/indexing-api/v3/prereqs#create-service-account

Save the service account key to a file named `credentials.json` in the project folder.

4. Add the service account to the project and give it the `Owner`
   role: https://developers.google.com/search/apis/indexing-api/v3/prereqs#verify-site


5. Change the sitemap URL in the `index.py` file:

```python
website_sitemap = 'https://example.com/sitemap.xml'
```

6. Run the script using the following command:

```shell
python index.py
```

## Questions and Issues

If you have any questions or issues, please open a new issue.