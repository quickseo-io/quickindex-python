# A Python script to quickly index your pages in Google Search

Made by [QuickIndex](https://quickindex.co) — A service to automatically index 1000s of pages in Google Search.

## Introduction

This is a Python script that uses the Google Indexing API to index your pages in Google Search. It's a simple script that you can run on your computer to index up to 200 pages per day in Google Search. The detailed description of the script is available in [here](https://quickindex.co/tools/python-indexing).



## Usage

1. Install the required packages using the following command:

```shell
pip install -r requirements.txt
```

2. Create a Project in the [Google Cloud Console](https://console.cloud.google.com/)


3. Create service account in Google
Cloud: [https://developers.google.com/search/apis/indexing-api/v3/prereqs#create-service-account](https://developers.google.com/search/apis/indexing-api/v3/prereqs#create-service-account)

Save the service account key to a file named `credentials.json` in the project folder. This service account will allow you to **index 200 pages per day** (this is Google API limitation).

4. Add the service account to the Google Search Console project and give it the `Owner`
role: [https://developers.google.com/search/apis/indexing-api/v3/prereqs#verify-site](https://developers.google.com/search/apis/indexing-api/v3/prereqs#verify-site)


5. Change the sitemap URL in the `index.py` file:

```python
website_sitemap = 'https://example.com/sitemap.xml'
```

The script will index all the pages from the sitemap. It will also find all the sitemaps in the sitemap index file and index all the pages from them.

6. Run the script using the following command:

```shell
python index.py
```

The script will index up to 200 pages per run. It automatically saves all the pages and whether they were submitted to Google in the `urls.json` file. This way, you can run the script multiple times, and it will only submit the pages that were not submitted to Google yet. You can run the script every day to index 200 pages per day.

Hope this helps you to index your pages in Google automatically.

## Questions and Issues

If you have any questions or issues, please open a new issue.