from rest_framework import serializers
from .models import *

class FineDustSerializer(serializers.ModelSerializer):
    class Meta:
        model = FineDust
        fields = ('id', 'place', 'value', 'date')


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowStatus
        fields = ['windowstatus']