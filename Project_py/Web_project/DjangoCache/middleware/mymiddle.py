import random
import time

from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_exception(self, request, exception):
        print("the exception is ")
        print(request, exception)
        return redirect(reverse('index'))

    def process_request(self, request):
        ipaddr = request.META.get("REMOTE_ADDR")
        print(ipaddr)
        if request.path == "/mycache/ticket/":
            if ipaddr.startswith("127"):
                return HttpResponse("请排队！")

        if request.path == "/mycache/jokers/":
            if ipaddr == "127.0.0.1":
                return HttpResponse("没有笑话")

        if request.path == "/mycache/blank/":
            cache = caches['redis_backend']

            blank_list = cache.get("blank", [])
            print(blank_list)

            if ipaddr in blank_list:
                return HttpResponse("你在黑名单")
            requests = cache.get(ipaddr, [])
            print(requests)
            while requests and time.time() - requests[-1] > 60:
                requests.pop()

            requests.insert(0, time.time())
            cache.set(ipaddr, requests, 60)

            if len(requests) > 30:
                blank_list.append(ipaddr)
                cache.set("blank", blank_list, timeout=60*60*24)
                return HttpResponse("see you tomorrow!")

            if len(requests) > 10:
                return HttpResponse("请60s后访问")

