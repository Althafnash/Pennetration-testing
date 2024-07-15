import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# https://www.yahoo.com

visited_urls = set()

def spider_urls(url, keyword):
    if url in visited_urls:
        return
    
    visited_urls.add(url)
    
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed: {url} - {e}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        a_tags = soup.find_all("a")
        urls = []
        for tag in a_tags:
            href = tag.get("href")
            if href is not None and href != "":
                full_url = urljoin(url, href)
                urls.append(full_url)
        #print(urls)

        for urls2 in url :
            if urls2 not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url , url)#
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join,keyword)
            else:
                pass

url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword to search in the URL: ")
spider_urls(url, keyword)
