from quickindex.sitemaps import fetch_urls_from_sitemap_recursive
from quickindex.utils import load_json, save_urls_to_file
from quickindex.indexing import index_url

website_sitemap = 'https://example.com/sitemap.xml'
urls = fetch_urls_from_sitemap_recursive(website_sitemap)

print('Total URLs:', len(urls))

# Add new urls to 'urls.json' file in the format {'url': true/false}.
# True means the URL is indexed and False means it is not indexed.

# read the existing urls from the file
existing_urls = load_json('urls.json')

# add only new urls to the file with the value set to False
for url in urls:
    if url not in existing_urls:
        existing_urls[url] = False

# save the updated urls to the file
save_urls_to_file(existing_urls, 'urls.json')

print('New URLs added to file')

# take up to 200 urls that are not indexed and index them
urls_to_index = [url for url, indexed in existing_urls.items() if not indexed][:200]

print('Total URLs to index:', len(urls_to_index))

# index the urls
for url in urls_to_index:
    result = index_url(url, 'credentials.json')
    if result:
        existing_urls[url] = True

# save the updated urls to the file
save_urls_to_file(existing_urls, 'urls.json')
