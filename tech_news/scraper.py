import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    string_split = reading_time.split()
    summary = selector.css(".entry-content > p:first-of-type ::text").getall()
    summary = ''.join(summary).strip()
    category = selector.css(".label::text").get()

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(string_split[0]),
        "summary": summary,
        "category": category,
    }

    return data


# Requisito 5
def get_tech_news(amount: int):
    get_url = "https://blog.betrybe.com/"
    tech_news = []
    while len(tech_news) < amount:
        content = fetch(get_url)
        links = scrape_updates(content)

        for link in links:
            if len(tech_news) >= amount:
                break

            tech_news.append(scrape_news(fetch(link)))
            get_url = scrape_next_page_link(content)
    create_news(tech_news)
    return tech_news
