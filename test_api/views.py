from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework import generics
import json
from .forms import PostForm
from .models import *
from .serializers import *


class TestAPIView(generics.ListAPIView):
    queryset = TempForms.objects.all()
    serializer_class = TempFormsSerializer

    def post(self):
        return print('dgsds')
        print('gdhfdh')

class TestView(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'base.html'

    def get(self,request):
        form=PostForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'test_api/base.html', context)
    # def post(self,request):
    #
    #     name = self.request.POST['name']
    #     listRes = dict(map(lambda x:x.split('='), name.split('&'))) #dict(name.split("="))
    #     print(self.request.POST)
    #return render(request, self.template_name, {'form': form})