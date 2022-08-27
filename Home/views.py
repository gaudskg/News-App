from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Article
from .utils import get_news_from_api
# Create your views here.
def home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-07-27&sortBy=publishedAt&apiKey=92e902d2a1c6450a8f895e36ca9873bc'
    #get_news_from_api(url)
    return render(request,'home.html', context={'articles': Article.objects.all()})