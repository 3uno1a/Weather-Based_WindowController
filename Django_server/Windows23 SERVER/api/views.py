from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render

# ModelViewSet을 상속받아 모델의 조회, 생성, 업데이트, 삭제와 같은 기능을 제공 

class ODUltraFineDustViewSet(viewsets.ModelViewSet):
    queryset = ODUltraFineDust.objects.all().order_by('-id') 
    serializer_class = ODUltraFineDustSerializer

class IDUltraFineDustViewSet(viewsets.ModelViewSet):
    queryset = IDUltraFineDust.objects.all().order_by('-id') 
    serializer_class = IDUltraFineDustSerializer


class TempViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all().order_by('-id') 
    serializer_class = TempSerializer


class RainViewSet(viewsets.ModelViewSet):
    queryset = Rain.objects.all()
    serializer_class = RainSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = Rain.objects.all()
        queryset.delete()        # 이전 데이터 모두 삭제

        response = super().create(request, *args, **kwargs)

        return response


class WindowViewSet(viewsets.ModelViewSet):
    queryset = WindowStatus.objects.all()
    serializer_class = WindowSerializer

    def create(self, request, *args, **kwargs):
        queryset = WindowStatus.objects.all()
        queryset.delete()        # 이전 데이터 모두 삭제

        response = super().create(request, *args, **kwargs)

        return response
    

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = Emotion.objects.all()
        
        if queryset.count() >= 2:                      
            queryset.first().delete()                   
        return response


class SpeechViewSet(viewsets.ModelViewSet):
    queryset = SpeechResult.objects.all().order_by('-id') 
    serializer_class = SpeechSerializer