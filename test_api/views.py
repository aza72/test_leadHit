import re
from urllib.parse import urlencode

from django.db.models import Q, Count
from rest_framework.response import Response
from rest_framework.views import APIView

from test_api.models import TempForms, NameTemp
from test_api.serializers import TempFormsSerializer


class TestView(APIView):

    def post(self,request):
        d = urlencode(request.GET)
        p = dict(map(lambda x: x.split('='), d.split('&')))
        data = check_form(p)
        form_search_cond = Q()  # django.db.models.Q
        for k, v in data.items():
            print(k)
            print(v)
            #form_search_cond &= Q(**{f'sample__{k}': v})
            form_search_cond.add(Q(name_field=k) & Q(name_type=v), Q.OR)
        print(form_search_cond)
        template = TempForms.objects.filter(form_search_cond)
        cont = template.filter()
        for p in template:
            c = TempForms.objects.filter(name_temp=p.name_temp).count()
            print(c)

        if template:
            serializer = TempFormsSerializer(template, many=True)
            #print(serializer.data)
            #print(template)
            return Response(serializer.data)
        else:
            return Response(data)


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

