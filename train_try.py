"""
@author: MsWon
@editor: lumyjuwon
"""

import time  ##시간설정을 위한 시간 모듈
import tensorflow as tf ## 머신러닝을 위한 모듈
import numpy as np  ##벡터(리스트)모듈
import Bi_LSTM ##학습모델
import Word2Vec  ##벡터화모델
import mariadb ## db연동 maria.db모듈
from konlpy.tag import Okt  ##konlpy에서 OKt형태소 분석기 사용
import sys ##파이썬 대화형 프롬프트사용을 위한 모듈
import os ##작업 디렉토리 지정을 위한 모듈
os.chdir('C:\\Users\\taddy\\run\\Data\\')
twitter = Okt()
W2V = Word2Vec.Word2Vec()

twitter = Okt()

def dbconnect():
        conn = mariadb.connect(
            user="root",
            password="yurii1205",
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
    db_result = []
    for i in result:
        db_result.append([i[0], category])
    return db_result

cat = ['body', 'comm', 'social', 'art', 'science']
line=[]

conn = dbconnect()
try:
    for i in cat:
        line += value(conn,i)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
token = []
embeddingmodel = []

for i in line:
    content = i[1]  # csv에서 뉴스 제목 또는 뉴스 본문 column으로 변경
    sentence = twitter.pos(i[0], norm=True, stem=True)
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
    
print("토큰 처리 완료")
tokens = np.array(token)
print("token 처리 완료")
print("train_data 최신 버전인지 확인")

train_X = tokens[:, 0]
train_Y = tokens[:, 1]
train_Y_ = W2V.One_hot(train_Y)  # Convert to One-hot
train_X_ = W2V.Convert2Vec('post.embedding',train_X)  # import word2vec model where you have trained before
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


X = tf.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.placeholder(tf.int32, shape = [None])


BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)


with tf.variable_scope("loss", reuse = tf.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)


prediction = tf.nn.softmax(logits)
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()


total_batch = int(Total_size / Batch_size)

print("Start training!")

modelName = "Bi_LSTM.model"
saver = tf.train.Saver()



with tf.Session() as sess:

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