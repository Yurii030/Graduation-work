import numpy as np
import gensim
from eunjeon import Mecab
from konlpy.tag import Okt

## 머신러닝에 사용할 단어들을 토크나이징, 벡터화, 제로 패딩 할 때 사용하는 클래스
class Word2Vec():
    
    def __init__(self):
        None

    def tokenize(self, doc): ## 토크나이징 과정 (문장 속 단어 사이에 '/' 토큰 추가해서 반환)
        pos_tagger = Mecab(dicpath='C:/mecab/mecab-ko-dic')
        return ['/'.join(t) for t in pos_tagger.pos(doc)]
    
    def read_data(self, filename):  ## 파일을 불러오는 함수같은데 사용하지 않는듯..
        with open(filename, 'r',encoding='utf-8') as f:
            data = [line.split('\t') for line in f.read().splitlines()]
            data = data[1:]
        return data
    
    def Word2vec_model(self, model_name): ## 워드투벡터 모델 불러오는 함수
        
        model = gensim.models.word2vec.Word2Vec.load(model_name)
        return model
    
    def Convert2Vec(self, model_name, doc): # 말뭉치를 벡터화하는 함수 - doc은 문장에 대한 단어 리스트임 ['i/morp', 'am/morp', 'ironman/morp'] ...
        #train_X_ = W2V.Convert2Vec("Word2Vec_csv_article.embedding",train_X)
        word_vec = []
        model = gensim.models.word2vec.Word2Vec.load(model_name)
        for sent in doc:  ## 말뭉치속 문장을 반복 (sent 는 하나에 문장에 대한 단어 리스트)
            sub = []
            for word in sent:  ## 하나의 문장 속 단어를 반복
                if word in model.wv.vocab:  ## 단어가 워드투벡터 모델에 있을경우
                    sub.append(model.wv[word]) # Word Vector Input
                else:  ## 없을경우 랜덤 벡터로 대체
                    sub.append(np.random.uniform(-0.25,0.25,300)) # used for OOV words
            word_vec.append(sub)
        
        return word_vec
    
    ## 자연어 처리 시 각 문장의 길이가 다르기 때문에 길이를 동일하기 하기 위해 0으로 채워주는 함수
    def Zero_padding(self, train_batch_X, Batch_size, Maxseq_length, Vector_size):
        
        zero_pad = np.zeros((Batch_size, Maxseq_length, Vector_size)) ## 0으로 구성된 넘파이 배열 생성 (여기선 (32, 가장 긴 문장의 길이, 300))
        for i in range(Batch_size):  ## batch_size 만큼 반복 - 여기선 32번
            try:
                zero_pad[i,:np.shape(train_batch_X[i])[0],:np.shape(train_batch_X[i])[1]] = train_batch_X[i]
            except:
                print(train_batch_X[i])
        return zero_pad
    
    ## 원 핫 인코딩 함수
    def One_hot(self, data):  ## 카테고리들은 원 핫 인코딩방식으로 인코딩
        
        index_dict = {value:index for index,value in enumerate(set(data))}  ## data의 집합(set) 즉 카테고리를 딕셔너리 형태로 저장
        ## indext_dict의 형태는 {0:0, 1:1, ..., 7:7}
        result = []
        
        for value in data:
            
            one_hot = np.zeros(len(index_dict)) ## 카테고리 갯수 만큼의 0으로 이루어진 넘파이 배열
            index = index_dict[value]  ## 카테고리 리스트에서 카테고리명을 통해 인덱스(숫자)를 추출
            one_hot[index] = 1 ## 넘파이 배열에서 카테고리 인덱스에 맞게 변경 ex([0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0])
            result.append(one_hot)  ## 넘파이 배열을 리스트에 삽입
        
        return result ## 넘파이 배열로 만들어진 카테고리 인덱스를 반환