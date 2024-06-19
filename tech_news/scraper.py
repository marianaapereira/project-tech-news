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
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next::attr(href)").get()

    if not next_page_link:
        return None

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    return {
        'url': selector.css("div::attr(data-share-url)").get(),
        'title': selector.css("h1.entry-title::text").get().strip(),
        'timestamp': selector.css("li.meta-date::text").get(),
        'writer': selector.css("span.author a::text").get(),
        'reading_time': int(
            selector.css("li.meta-reading-time::text")
            .get()
            .split()[0]
        ),
        'summary': (
            ''.join(
                selector.css('.entry-content > p:first-of-type *::text')
                .getall()
            )
            .strip()
        ),
        'category': selector.css("span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
