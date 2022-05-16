"""
@author: MsWon
@editor: lumyjuwon
"""

import time ##시간설정을 위한 시간 모듈
import tensorflow as tf ## 머신러닝을 위한 모듈
import numpy as np ##벡터(리스트)모듈
import Bi_LSTM as Bi_LSTM ##학습모델
import Word2Vec as Word2Vec ##벡터화모델
import mariadb ## db연동 maria.db모듈
from konlpy.tag import Okt ##konlpy에서 OKt형태소 분석기 사용
import sys ##파이썬 대화형 프롬프트사용을 위한 모듈
import os ##작업 디렉토리 지정을 위한 모듈
os.chdir('E:\\senier_project\\run\\Data\\')
twitter = Okt() ##Okt객체 생성 메서드
W2V = Word2Vec.Word2Vec()

twitter = Okt() ## Okt객체 생성 메서드
## 데이터 베이스 정보
def dbconnect():
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="category"
            )
        return conn

def value(conn,category):
    cur = conn.cursor()
    # connection 객체로부터 cursor()메서드를 호출
    sql=sql = "SELECT * FROM " + category
    cur.execute(sql) # 데이터 행의 개수
    result= cur.fetchall()
    ## fetchall() : 바로 레코드를 배열형식으로 저장해 주는 일을 함.
    db_result = []
    for i in result:
        db_result.append([i[0], category])
         ## shape=[None]-> None은 크기가 정해지지 않았음을 뜻함.
    return db_result
#영역분류
cat = ['body', 'comm', 'social', 'art', 'science']
line=[]

conn = dbconnect() ## db연결
##예외처리
try:
    for i in cat:
        ## cat함수 : 원하는 dimension방향으로 텐서를 나란하게 쌓아준다.
        ## dimension : x축,y축 등으로 나타내는 축.
        line += value(conn,i)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
token = []
embeddingmodel = []

for i in line:
    content = i[1]  # csv에서 뉴스 제목 또는 뉴스 본문 column으로 변경
    sentence = twitter.pos(i[0], norm=True, stem=True) ##원형을 찾아주는 옵션(norm,stem)
    ## pos : 찾는 문자열의 위치가 일정하지 않을 경우(copy 함수를 쓸 수 없는 경우) 사용할 수 있다.
    temp = []
    temp_embedding = []
    all_temp = []
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category = i[1]  # csv에서 category column으로 변경
    category_number_dic = {'body': 0, 'comm': 1, 'social': 2, 'art': 3, 'science': 4}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp)
    ##apend함수 : 목록 끝에 요소 추가
    
print("토큰 처리 완료")
tokens = np.array(token)
print("token 처리 완료")
print("train_data 최신 버전인지 확인")
train_X = tokens[:, 0]
## train_X.shape : 데이터 사이즈를 나타냄
## train_X : 데이터 사이즈나타냄
train_Y = tokens[:, 1]
print('확인1')
train_Y_ = W2V.One_hot(train_Y)  # Convert to One-hot
## w2V.One_hot : 단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을
## 부여하고, 다른 인덱스에는 0을 부여하는 벡터 표현의 방식이다.
train_X_ = W2V.Convert2Vec("post.embedding",train_X)  # import word2vec model where you have trained before
print('확인2')
Batch_size = 32
Total_size = len(train_X)
Vector_size = 300
seq_length = [len(x) for x in train_X]
Maxseq_length = max(seq_length)
print('확인3')
learning_rate = 0.001
lstm_units = 128
## ** 카테고리 개수 지정 ** ##
num_class = len(cat)
## ** 학습 반복 횟수 지정 ** ##
training_epochs = 15
## epoch : 전체 데이터를 1회 훑어 학습하는 것.
## epochs : 전체 sample 데이터를 한 바퀴 돌며 학습하는 것을 1 epoch라고 한다.
keep_prob = 0.75
## keep_prob값은 dropout 시 뉴런을 얼마나 남길 것인지를 결정하는 매개변수
## 예를 들면 keep_prob = 0.8이라 가정했을 때, 이는 각층마다 80%확률로 뉴런을 유지하고, 20%확률로 뉴런을 제거한다는 의미이다.
X = tf.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
 ## tf.placeholder : 재료를 담는 그릇(만약 이미지 학습시 이미지의 픽셀값이 저장되는 공간임)
 ## tf.float32 : 변수의 데이터타입 지정, max_seq_length : 토큰 기준 입력 문장 최대 길이(지문,질문 모두 포함)

print('확인4')
Y = tf.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
## tf.placeholder : 재료를 담는 그릇(만약 이미지 학습시 이미지의 픽셀값이 저장되는 공간임)
## shape은 입력 데이터의 형태를 의미한다. //  ## shape=[None]-> None은 크기가 정해지지 않았음을 뜻함.
## 상수가 될 수도 있고 다차원배열의 정보가 들어올 수도 있음(디폴트 파라미터로 None 지정)
## name : 해당 placeholder의 이름을 부여하는 것으로 적지 않아도 되긴함(디폴트 파라미터로 none지정)
print('확인5')
seq_len = tf.placeholder(tf.int32, shape = [None])
 ## tf.placeholder : 재료를 담는 그릇(만약 이미지 학습시 이미지의 픽셀값이 저장되는 공간임)
 ## tf.int32 : 변수의 데이터 타입 지정, shape =[None]
 ## seq_len(N) : 1~N까지 숫자형 벡터 반환
 ## shape=[None]-> None은 크기가 정해지지 않았음을 뜻함. 
 ## 일단 만들고 난 다음 나중에 크기를 정하겠다라는 뜻

print('확인6')

BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)
print('확인7')

with tf.variable_scope("loss", reuse = tf.AUTO_REUSE):
    ## tf.variable_scope(<name>,<shape>,<initializer>) 
    ## : 입력된 이름의 변수를 생성하거나 반환한다.

    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)
print('확인8')

prediction = tf.nn.softmax(logits)
## softmax함수 : 분류될 클래스가 n개라 할때, n차원의 벡터를 입력받아, 각 클래스에 속할 확률을 추정한다.
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
## tf.equal : 둘이 같으면 true // tf.argmx(a,1) : 인덱스 개수가 2라고 설정했을 때 인덱스 [2,1]이 가장크다라고 할 수 있음
## 즉 tf.argmx(prediction,1)은 [prediction,1]이 가장큼.
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
## tf.reduce_mean : 차원을 감소하며 평균을 구한다.
## tf.cast : 텐서를 새로운 형태로 캐스팅하는데 사용, 부동소수점형에서 정수형ㅇ로 바꾼경우 소수점을 버린다
## boolean 형태의 경우 True이면 1, false이면 0을 출력한다.
print('확인9')
init = tf.global_variables_initializer()
## tf.gloabal_variables_initializer() : 모델의 모든 변수를 초기화함, 하지만 사용자가 직접초기화할 변수 리스트를 만들 수도 있음.
## Variables Documentation에서 변수 초기화 여부를 확인하는 기능을 포함한 옵션을 볼 수 있음.
print('확인10')

total_batch = int(Total_size / Batch_size)
print('확인11')
print("Start training!")

modelName = "Bi_LSTM.model"
saver = tf.train.Saver()



with tf.Session() as sess:
    ## tf.Session() as sess=> 세션 선언문(sess라는 변수에 세션하나 할당하겠다.)

    start_time = time.time()
    sess.run(init)
    train_writer = tf.summary.FileWriter('Bidirectional_LSTM', sess.graph)
    i = 0
    for epoch in range(training_epochs):

        avg_acc, avg_loss = 0. , 0.
        for step in range(total_batch):
            ## batch_size : 배치 크기. 하드웨어 가속기로 GPU를 선택
            train_batch_X = train_X_[step*Batch_size : step*Batch_size+Batch_size]
            train_batch_Y = train_Y_[step*Batch_size : step*Batch_size+Batch_size]
            batch_seq_length = seq_length[step*Batch_size : step*Batch_size+Batch_size]
            
            train_batch_X = W2V.Zero_padding(train_batch_X, Batch_size, Maxseq_length, Vector_size)
            ## Batch size : 1 Step에서 사용한 데이터 개수이다. 가령 SGD의 batch size는 1이다.
            ## Step : 1개의 배치로부터 loss를 계산한 후, Weight와 Bias를 1회 업데이트하는 것을 1Step이라 한다.
            ## Step : 파라미터 1회를 업데이트 하는거.
            ## loss : 손실함수에 대입한 결과와 실제 정답간의 간격,즉 차이를  loss라고 한다.
            ## weight : 중요도 // bias : 성향 
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
