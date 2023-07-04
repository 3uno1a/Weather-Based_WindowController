from django.db import models

class ODUltraFineDust(models.Model):       # 실외 초미세먼지 
    value = models.FloatField() 
    date = models.DateTimeField() 

class IDUltraFineDust(models.Model):       # 실내 초미세먼지 
    value = models.FloatField() 
    date = models.DateTimeField() 

class Temp(models.Model):     # 실외 온도
    value = models.FloatField() 
    date = models.DateTimeField() 

class Rain(models.Model):    # 비가 오는지 안오는지
    rainstatus = models.BooleanField(default = False)

class WindowStatus(models.Model):     # 창문 개폐 상태
    windowstatus = models.BooleanField(default = False)

class Emotion(models.Model):        # 감정 (긍정/부정)
    emotion = models.BooleanField(default = True)

class SpeechResult(models.Model):       # stt 결과
    date = models.DateTimeField(auto_now_add = True)      # 날짜 시간 자동 저장
    text = models.TextField()
