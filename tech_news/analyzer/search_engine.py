from ..database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    found_news = search_news(query)

    if not found_news:
        return []

    result_news_list = []

    for news in found_news:
        result_news_list.append((
            news['title'],
            news['url']
        ))

    return result_news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
