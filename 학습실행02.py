## 학습 과정
"""
임베딩한 데이터와 Bi_LSTM 모델을 이용해 머신러닝을 진행하는 과정
"""
## ** PART 2 . 임베딩된 학습 데이터를 Bi_LSTM 모델을 통해 학습 ** ##
import import_ipynb ## ipynb 파일을 불러오기 위한 모듈
import time  ## 작업 시간 측정을 위한 모듈
import os    ## 작업 디렉토리 지정을 위한 모듈
import random ## 리스트 셔플을 위한 모듈
import mysql.connector   ## 데이터베이스에 접근하기 위한 모듈
import tensorflow as tf  ## 머신러닝을 위한 모듈
import numpy as np  ## 머신러닝에 사용할 데이터 구조화를 위한 모듈
import Bi_LSTM as Bi_LSTM  ## 머신러닝 모듈
import Word2Vec as Word2Vec  ## 벡터화 모듈
from eunjeon import Mecab  ## 형태소 분석기 모듈
from konlpy.tag import Okt

## 데이터베이스에 접속해 카테고리별 제목 리스트를 카테고리와 함께 반환
def conn_DB(category):
    ## 전역에 지정된 데이터베이스 정보 변수
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

## 작업 디렉토리 설정 (머신러닝 모듈이 저장될 위치) ##
os.chdir('C:\\anaconda\\morpy\\Bi_LSTM\\data')
## 단어 벡터화 모듈 선언 ##
W2V = Word2Vec.Word2Vec()
## 형태소 분석기 선언 (사용자 사전 위치 지정) ##
mc = Mecab(dicpath='C:/mecab/mecab-ko-dic')
okt = Okt()
## 데이터베이스 정보
config = {
    "user": "yourID",
    "password": "yourPW",
    "host": "yourURL", #local
    "database": "data", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

## 사용할 카테고리 리스트 (데이터베이스 테이블 이름과 동일하게 해야함)
cat = ['body', 'comm', 'social', 'art', 'science']
unity = []
## 카테고리별로 데이터베이스 접속 함수를 통해 리스트 통합
for i in cat:
    tmp = conn_DB(i)
    unity += tmp
## 리스트 셔플
random.shuffle(unity)
random.shuffle(unity)

## 임베딩 과정
token = []
embeddingmodel = []
print("Start tokenizing\n")
for i in unity:
    content = i[0]  ## Title (default : 0)
    sentence = mc.pos(content) ## Morph
    temp = []
    temp_embedding = []
    all_temp = []
    
    ## Morph list
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
        
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category = i[1]  ## category (default : 1)
    ## ** 해당 딕셔너리를 카테고리에 맞게 지정 ** ##
    category_number_dic = {'body': 0, 'comm': 1, 'social': 2, 'art': 3, 'science': 4}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp)
    
tokens = np.array(token) ## 넘파이 배열로 저장
print("Tokenizing complete\n")

train_X = tokens[:, 0]  ## 전체 문장에 대한 단어 리스트 (['i/morp', 'am/morp', 'ironman/morp'])

train_Y = tokens[:, 1]  ## 전체 문장에 대한 카테고리 (문장 갯수만큼)


train_Y_ = W2V.One_hot(train_Y)  # Convert to One-hot - 카테고리 인덱스 리스트

train_X_ = W2V.Convert2Vec("post.embedding", train_X)  # import word2vec model where you have trained before - 벡터화된 단어

Batch_size = 32
Total_size = len(train_X)
Vector_size = 300
seq_length = [len(x) for x in train_X]
Maxseq_length = max(seq_length)
learning_rate = 0.001
lstm_units = 128
## ** 카테고리 개수 지정 ** ##
num_class = len(cat)
## ** 학습 반복 횟수 지정 ** ##
training_epochs = 15
keep_prob = 0.75

X = tf.placeholder(dtype=tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.placeholder(dtype=tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.placeholder(tf.int32, shape = [None])
BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)
## get_variable() 에서 생성된 'loss' 변수를 관리하는 함수
with tf.variable_scope("loss", reuse = tf.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)

prediction = tf.nn.softmax(logits)
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()

total_batch = int(Total_size / Batch_size)

print("Start training!")
## 저장될 모델 이름 지정 ##
modelName = "Bi_LSTM.model"
## 모델 저장을 위해 선언 ##
saver = tf.train.Saver()
## 학습 시작 ##
with tf.Session() as sess:
    ## 학습 시간을 확인하기 위해 현재 시간 저장 ##
    start_time = time.time()
    sess.run(init)
    train_writer = tf.summary.FileWriter('Bidirectional_LSTM', sess.graph)
    i = 0
    for epoch in range(training_epochs):

        avg_acc, avg_loss = 0. , 0.
        for step in range(total_batch):

            train_batch_X = train_X_[step*Batch_size : step*Batch_size+Batch_size]
            train_batch_Y = train_Y_[step*Batch_size : step*Batch_size+Batch_size]
            batch_seq_length = seq_length[step*Batch_size : step*Batch_size+Batch_size]
            train_batch_X = W2V.Zero_padding(train_batch_X, Batch_size, Maxseq_length, Vector_size)
            sess.run(optimizer, feed_dict={X: train_batch_X, Y: train_batch_Y, seq_len: batch_seq_length})
            # Compute average loss
            loss_ = sess.run(loss, feed_dict={X: train_batch_X, Y: train_batch_Y, seq_len: batch_seq_length})
            avg_loss += loss_ / total_batch
            
            acc = sess.run(accuracy , feed_dict={X: train_batch_X, Y: train_batch_Y, seq_len: batch_seq_length})
            avg_acc += acc / total_batch
            print("epoch : {:02d} step : {:04d} loss = {:.6f} accuracy= {:.6f}".format(epoch+1, step+1, loss_, acc))

        summary = sess.run(BiLSTM.graph_build(avg_loss, avg_acc))
        train_writer.add_summary(summary, i)
        i += 1

    duration = time.time() - start_time
    minute = int(duration / 60)
    second = int(duration) % 60
    print("Train complete\n")
    print("%dminutes %dseconds\n" % (minute,second))
    save_path = saver.save(sess, modelName)
    train_writer.close()
    print(save_path)
    print('Model saved')
