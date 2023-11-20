import re
from urllib.parse import urlencode
from rest_framework.response import Response
from rest_framework.views import APIView
from test_api.serializers import TempFormsSerializer


class TestView(APIView):

    def post(self,request):
        d = urlencode(request.GET)
        p = dict(map(lambda x: x.split('='), d.split('&')))
        data = check_form(p)
        serializer = TempFormsSerializer(data, many=True)
        print(serializer.data)
        return Response(serializer.data)


def check_type(data):
    test = {'date': r'^\d\d\.\d\d\.\d{4}$',
            'phone': r'^\+79\s*\d{2}\s*\d{3}\s*\d{2}\s*\d{2}$',
            'email': r'^\S+@\w+.\w{2,4}$',
            }

    for types, rex in test.items():
        if re.fullmatch(rex, data):
            print(types)
            return types

    return 'text'
def check_form(data):
    #print(data)
    res = {}
    #data = data.dict()
    #print(data)
    for k, v in data.items():
        #v = urlencode(v)
        print(v)
        res[k] = check_type(v)
        #print(v)
    return res

