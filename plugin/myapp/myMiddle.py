#!/usr/bin/env python
# coding:utf-8
from django.utils.deprecation import MiddlewareMixin

class MyPlugin(MiddlewareMixin):
    def process_request(self, request):
        print("get参数为：{}".format(request.GET.get("a")))

