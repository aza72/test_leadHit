import re

from django.db.migrations import serializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from rest_framework.views import APIView
from test_api.models import TempForms
from test_api.serializers import TempFormsSerializer


class TestView(APIView):

    def post(self,request):

        #d = request.POST
        data = check_form(request.GET)
        #data = TempForms.objects.all()
        serializer = TempFormsSerializer(data, many=True)
        print(serializer.data)
        return Response(serializer.data)


def check_type(data):
    test = {'date': r'^\d\d\.\d\d\.\d{4}$',
            'phone': r'^(\+79\d{9})$',
            'email': r'^\S+@\w+.\w{2,4}$',
            }

    for types, rex in test.items():
        if re.fullmatch(rex, data):
            #print(types)
            return types

    return 'text'
def check_form(data):
    res = {}
    data = data.dict()
    for k, v in data.items():
        res[k] = check_type(v)
        print(v)
    return res

