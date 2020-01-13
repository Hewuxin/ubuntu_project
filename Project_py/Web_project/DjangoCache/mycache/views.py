import time
from time import sleep

from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse("index")


@cache_page(60, cache='default')
def news(request):
    news_list = []
    for i in range(10):
        news_list.append("hahahha%d" % i)
    sleep(5)
    return render(request, 'news.html', context={"news_list": news_list})


def joker(request):
    cache = caches['redis_backend']
    res = cache.get("jokers")
    if res:
        return HttpResponse(res)
    sleep(5)

    joker_list = []
    for i in range(10, 20):
        joker_list.append("hahahahaha joker joker %d" % i)
    data = {
        'title': "hahahahaha",
        'joker_list': joker_list
    }
    response = render(request, "jokers.html", context=data)
    cache.set("jokers", response.content, timeout=60)
    return response


def adds(request):
    a = 5 / 0
    return HttpResponse(a)


def ticket(request):

    return HttpResponse("you get a ticket successfully")


def blank(request):
    cache = caches['redis_backend']
    res = cache.get("data")
    if res:
        return HttpResponse(res)
    time.sleep(5)
    data = "欢迎访问"
    cache.set("data", data,  timeout=60)
    return HttpResponse(data)
