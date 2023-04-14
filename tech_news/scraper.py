import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=4
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.ReadTimeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    if not len(links) == 0:
        return links
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
