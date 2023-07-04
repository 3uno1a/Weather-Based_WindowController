# !pip install requests
# !pip install numpy
# !pip install prometheus_api_client
# !pip install scikit-learn
# !pip install matplotlib
# !pip install pyupbit 
# !pip install pydot

import numpy as np
import pandas as pd
import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import requests
import json
from tensorflow.keras.models import load_model

# 텍스트 가져오기
import requests 
def get_stt():
    url_speech = 'http://172.30.1.111:8000/api/speech/'

    response = requests.get(url_speech)
    if response.status_code == 200:
        data = response.json()
        print("API GET 요청 성공")
        return data[0]['text']
    else:
        print("API GET 요청 실패:", response.status_code)
        return None
    
text_data = get_stt()

# print(text_data)

#######################################################################
# 여기서부터 모델

okt = Okt()
tokenizer  = Tokenizer()

# DATA_CONFIGS = './data2/LSTM/data_configs.json'
DATA_CONFIGS = 'C:\workspace\django\windows23\AI\data2\LSTM\data_configs.json'
prepro_configs = json.load(open(DATA_CONFIGS,'r'))
word_vocab =prepro_configs['vocab']

tokenizer.fit_on_texts(word_vocab)

MAX_LENGTH = 30 #문장최대길이

sentence = text_data
sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\\s ]','', sentence)
stopwords = ['은','는','이','가','하','아','것','들','의','있','되','수','보','주','등','한'] # 불용어 추가할 것이 있으면 이곳에 추가
sentence = okt.morphs(sentence, stem=True) # 토큰화
sentence = [word for word in sentence if not word in stopwords] # 불용어 제거
vector  = tokenizer.texts_to_sequences(sentence)
pad_new = pad_sequences(vector, maxlen = MAX_LENGTH) # 패딩

# print(pad_new)
model = load_model('./data2/LSTM/model.h5') #모델 불러오기
# model.load_weights('./data2/LSTM/model.h5') #모델 불러오기
predictions = model.predict(pad_new)
predictions = float(predictions.squeeze(-1)[1])
# print(predictions)

result = ()

if(predictions > 0.5):
    # print(1) 
    result = 1
else:
    print(0)
    result = 0
# if(predictions > 0.5):
#   print("{:.2f}% 확률로 긍정 \n".format(predictions * 100))
# else:
#   print("{:.2f}% 확률로 부정 \n".format((1 - predictions) * 100))

#######################################################################
#post
def post_emotion(result):
    url_emotion = 'http://172.30.1.111:8000/api/emotion/'
    data_emotion = {
        'emotion': result,
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url_emotion, data=json.dumps(data_emotion), headers=headers)
    if response.status_code == 201:
        print("API POST 요청 성공")
    else:
        print("API POST 요청 실패")

post_emotion(result)


