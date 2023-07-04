from rest_framework import serializers
from .models import *

class ODUltraFineDustSerializer(serializers.ModelSerializer):
    class Meta:
        model = ODUltraFineDust
        fields = ('id', 'value', 'date')

class IDUltraFineDustSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDUltraFineDust
        fields = ('id', 'value', 'date')


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ('id', 'value', 'date')


class RainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rain
        fields = ['rainstatus']


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowStatus
        fields = ['windowstatus']


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ['emotion']


class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechResult
        fields = ('id', 'text', 'date')