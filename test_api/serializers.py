from rest_framework import serializers
from .models import *


class TempFormsSerializer(serializers.ModelSerializer):
    name_temp = serializers.CharField()
    class Meta:
        model = TempForms
        fields = ('name_temp', 'name_field', 'name_type')