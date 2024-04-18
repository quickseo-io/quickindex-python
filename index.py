from quickindex.sitemaps import fetch_urls_from_sitemap_recursive
from quickindex.utils import load_json, save_urls_to_file, APP_LOGGER
from quickindex.indexing import index_url

config = load_json("config.json")
APP_LOGGER.info(f"Started SITEMAP URL: {config['sitemap_url']}")

urls = fetch_urls_from_sitemap_recursive(config['sitemap_url'])
APP_LOGGER.info(f"Total URLs: {len(urls)}")

# Add new urls to 'urls.json' file in the format {'url': true/false}.
# True means the URL is indexed and False means it is not indexed.

# read the existing urls from the file
existing_urls = load_json("urls.json")

# add only new urls to the file with the value set to False
NEW_URLS = 0
for url in urls:
    if url not in existing_urls:
        NEW_URLS += 1
        existing_urls[url] = False

# check if the URL exists
DELETED_URLS = 0
for url in existing_urls:
    if url not in urls:
        DELETED_URLS += 1
        del existing_urls[url]

# save the updated urls to the file
save_urls_to_file(existing_urls, "urls.json")

if NEW_URLS:
    APP_LOGGER.info(f"New URLs added to file: {NEW_URLS}")

if DELETED_URLS:
    APP_LOGGER.info(f"Deleted URLs from file: {DELETED_URLS}")

# take up to 200 urls that are not indexed and index them
urls_to_index = [url for url, indexed in existing_urls.items() if not indexed][:200]

APP_LOGGER.info(f"Total URLs to index: {len(urls_to_index)}")

# index the urls
for i, url in enumerate(urls_to_index, 1):
    try:
        result = index_url(url, "credentials.json", i)
        if result:
            existing_urls[url] = True

    except Exception as e:
        existing_urls[url] = False
        APP_LOGGER.warning(f"Error indexing {url}: {e}")
        break

# save the updated urls to the file
save_urls_to_file(existing_urls, 'urls.json')
