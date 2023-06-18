from django.db import models

class FineDust(models.Model):       # 미세먼지 데이터
    place = models.CharField(max_length = 50)
    value = models.FloatField() 
    date = models.DateTimeField() 


class WindowStatus(models.Model):     # 창문 개폐 상태
    windowstatus = models.BooleanField(default = False)