import csv
from collections import Counter
import pandas as pd

# 1. 트윗터 패키지 안에 konlpy 모듈호출
from konlpy.tag import Twitter
twitter = Twitter()

# 2.파일 읽기
DEST = "./processed_data/"
comp_list=["compatibility.csv","incompatibility.csv"]
noun_list = []
for filename in comp_list:
    f = open(DEST+filename,'r',encoding='utf-8')
    rdr = csv.reader(f)

    # 3. 변수 okja에 문장들 저장
    okja=[]
    food_names=[]
    for line in rdr:
        okja.append(line[2])
        food_names.append(line[0])
        food_names.append(line[1])
    # 4. 각 문장별로 형태소 구분하기
    sentences_tag = []
    for sentence in okja:
        morph = twitter.pos(sentence)
        sentences_tag.append(morph)
    #    print(morph)
    #    print('-'*30)

    # 5. 명사만 선별해 리스트에 담기
   
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun']:
                noun_list.append(word)

    # 음식이름은 빼고 구하기 (set의 차집합)
    noun_list= list(set(noun_list)-set(food_names))
    
    # 6. 선별된 명사들 출력
    for word in noun_list:
        print(word)


# 컬럼명 달아주기
noun_list.insert(0,"DISEASE")

# 엑셀에 담기
dataframe = pd.DataFrame(noun_list)
dataframe.to_csv(DEST+'diseases.csv', header=False, index=False,encoding='utf-8-sig')

print(len(noun_list))
f.close() 
 