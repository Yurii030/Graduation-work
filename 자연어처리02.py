"""
자연어 처리를 위해 단어를 임베딩하는 과정
(자연어를 컴퓨터가 이해할 수 있는 벡터값으로 변환하는 과정)
--------------------------------------------------
크롤링한 문장들을 각각 형태소 분석을 통해 단어 추출
추출한 단어를 토큰화한 후 임베딩 실시 (벡터화)
--------------------------------------------------
"""
import mysql.connector      ## 데이터베이스에 접근하기 위한 모듈
import random               ## 리스트 셔플을 위한 모듈
import os                   ## 작업 디렉토리 지정을 위한 모듈
from eunjeon import Khaii   ## 형태소 분석 모듈
from konlpy.tag import Okt
from gensim.models import Word2Vec   ## 단어 벡터화 모듈
## 임베딩 시각화 작업에 필요한 모듈들
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib as mpl
import matplotlib.pyplot as plt
## 작업 폴더 지정
os.chdir('C:\\anaconda\\morpy\\Bi_LSTM\\data')
## 형태소 분석기의 사용자 사전 위치 지정
mc = Mecab(dicpath='C:/mecab/mecab-ko-dic')
okt = Okt()
## 데이터베이스에 접근하기 위한 정보
config = {
    "user": "yourID",
    "password": "yourPW",
    "host": "yourURL", #local
    "database": "data", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

## 데이터베이스에 접근하여 카테고리별 제목 리스트를 가져와 레이블에 맞게 리스트 생성 및 반환 
## (0 : 제목, 1 : 카테고리)
def conn_DB(category):
    ## 전역 변수인 데이터베이스 정보
    global config
    try:
        #접속정보에 따른 데이터베이스 연동
        conn = mysql.connector.connect(**config)
        #커서 생성
        cursor = conn.cursor()
        #원하는 sql문 작성 (article 테이블 조회)
        sql = "SELECT * FROM " + category
        # cursor 객체를 이용해서 수행한다.
        cursor.execute(sql)
        # select 된 결과 셋 얻어오기
        resultList = cursor.fetchall()  # tuple 이 들어있는 list
        
    #예외처리
    except mysql.connector.Error as err:
        print(err)
    
    ## 카테고리와 함께 list로 만들어서 반환
    db_list = []
    for i in resultList:
        db_list.append([i[0], category])
    
    return db_list


## 카테고리에 맞게 수정
cat = ['body', 'comm', 'social', 'art', 'science']
unity = []
## 카테고리별로 데이터베이스에 접근하는 함수 호출
for i in cat:
    tmp = conn_DB(i)
    unity += tmp    ## 데이터베이스를 통해 받아온 리스트를 모두 합침
## 리스트 셔플
random.shuffle(unity)

## 임베딩 전 문장 형태소 분석 및 토큰화 과정 ##
token = []
print("Start tokenizing ...")
for i in unity:
    content = i[0]  ## title index (default : 0)
    sentence = mc.pos(content) ## morph
    temp = []
    all_temp = []
    
    ## morph list
    for k in range(len(sentence)):
        temp.append(sentence[k][0] + '/' + sentence[k][1]) ## 형태소 분석한 단어들과 형태(?)
    
    all_temp.append(temp)
    category = i[1]   ## category index (default : 1)
    category_number_dic = {'body': 0, 'comm': 1, 'social': 2, 'art': 3, 'science': 4}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp) ## 토큰의 형태는 단어/형태/카테고리번호로 구성되어있음
print("Tokenizing complete\n")

print("Start embedding ...")
## 최종 임베딩 데이터 구축 ##
embeddingmodel = []
for i in range(len(token)):
    temp_embeddingmodel = []
    for k in range(len(token[i][0])):
        temp_embeddingmodel.append(token[i][0][k])
    
    embeddingmodel.append(temp_embeddingmodel)

## Word2Vec 모듈을 통해 임베딩 ##
## iter 10번학습, sg : skip-gram 사용여부(1: 사용,other: CBOW), size : wordvec의 사이즈(현재는 300크기의 벡터스페이스), min_count : 5이하 출현한 단어는 무시, window 중심단어에서 주변 몇개의 단어를 예측할지 알아보는 변수
embedding = Word2Vec(embeddingmodel, size=300, window=5, min_count=3, iter=10, sg=1, max_vocab_size=360000000)
print(embedding)
embedding.save('post.embedding')
print("Embedding complete")