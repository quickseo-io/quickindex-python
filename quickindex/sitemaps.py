import requests
from bs4 import BeautifulSoup


def fetch_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        urls = [loc.text for loc in soup.find_all("loc")]
        return urls
    else:
        print(f"Failed to fetch sitemap: {sitemap_url}")
        return []


def fetch_urls_from_sitemap_recursive(sitemap_url, visited_sitemaps=set()):
    visited_sitemaps.add(sitemap_url)
    urls = fetch_urls_from_sitemap(sitemap_url)

    ALL_URLS = []

    for url in urls:
        if not url.endswith(".xml"):
            ALL_URLS.append(url)  # You can replace this with your desired processing

        # If the URL points to another sitemap, recursively fetch URLs from it
        if url.endswith(".xml") and url not in visited_sitemaps:
            fetch_urls_from_sitemap_recursive(url, visited_sitemaps)

    return ALL_URLS
