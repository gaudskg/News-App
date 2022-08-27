from urllib import response
import requests
from .models import *
def get_news_from_api(url):
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        if data.get('articles'):
            for article in data.get('articles'):
                source = article.get('source').get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                link = article.get('url')
                urlToImage = article.get('urlToImage')
                publishedAt = article.get('publishedAt')
                content = article.get('content')
                Article.objects.create(
                    source = source,
                    author = author,
                    title = title,
                    description = description,
                    url = link,
                    urlToImage = urlToImage,
                    publishedAt = publishedAt,
                    content = content
                )
    except Exception as e:
        print(e)