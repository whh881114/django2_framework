# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from rest_framework import generics
from django.http import JsonResponse


class Hello_V2(generics.ListCreateAPIView):
    def get(self, request):
        ret = {
            "status": "True",
            "code": 0,
            "msg": "Hello, world. I am %s. This is version 2." % request.META['REMOTE_ADDR']
        }

        return JsonResponse(ret, safe=False)