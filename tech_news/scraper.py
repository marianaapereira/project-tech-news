# Requisito 1
import requests
import time
from parsel import Selector


def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text

        else:
            return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css("h2 a::attr(href)").getall()

    if not news_links:
        return []

    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
