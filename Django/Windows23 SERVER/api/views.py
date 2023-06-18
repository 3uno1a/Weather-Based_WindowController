from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render

# ModelViewSet을 상속받아 모델의 조회, 생성, 업데이트, 삭제와 같은 기능을 제공 
class FineDustViewSet(viewsets.ModelViewSet):
    queryset = FineDust.objects.all()
    serializer_class = FineDustSerializer


class WindowViewSet(viewsets.ModelViewSet):
    queryset = WindowStatus.objects.all()
    serializer_class = WindowSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = WindowStatus.objects.all()

        if queryset.count() >= 2:                 # 데이터 생성시, 2개 이상이 되면 
            queryset.first().delete()             # 가장 먼저 만들어진 데이터부터 삭제
        return response