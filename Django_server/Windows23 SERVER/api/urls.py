from rest_framework import routers 
from .views import *
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

# 미세먼지
router.register('outdoor_ultrafine', ODUltraFineDustViewSet)
router.register('indoor_ultrafine', IDUltraFineDustViewSet)

router.register('temp', TempViewSet)
router.register('rain', RainViewSet)
router.register('window', WindowViewSet)
router.register('emotion', EmotionViewSet)
router.register('speech', SpeechViewSet)

app_name = 'api'

urlpatterns = [ 
    path('', include(router.urls)),
]
