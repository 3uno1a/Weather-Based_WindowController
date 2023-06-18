from rest_framework import routers 
from .views import *
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

router.register('finedust', FineDustViewSet)
router.register('window', WindowViewSet)

app_name = 'api'

urlpatterns = [ 
    path('', include(router.urls)),
]
