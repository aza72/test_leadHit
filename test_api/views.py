import re
from urllib.parse import urlencode
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from test_api.models import TempForms
from test_api.serializers import TempFormsSerializer


class TestView(APIView):

    def post(self,request):
        d = urlencode(request.GET)
        p = dict(map(lambda x: x.split('='), d.split('&')))
        #p=request.GET
        print(p)

        data = check_form(p)
        form_search_cond = Q()
        for k, v in data.items():
            form_search_cond.add(Q(name_field=k) & Q(name_type=v), Q.OR)
        template = TempForms.objects.filter(form_search_cond).select_related('name_temp')
        cont = []
        if template:

            for p in template:
                c = TempForms.objects.filter(name_temp=p.name_temp).count()
                d = template.filter(name_temp=p.name_temp).count()
                if d>=c:
                    cont.append(p.name_temp)
                    cont = list(set(cont))


        if cont:
            #x = NameTemp.objects.filter(name__in=cont)
            serializer = TempFormsSerializer(cont, many=True)
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
            return types

    return 'text'
def check_form(data):
    res = {}
    for k, v in data.items():
        res[k] = check_type(v)
    return res

