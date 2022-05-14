import tensorflow as tf  ## 머신러닝을 위한 모듈
import Bi_LSTM as Bi_LSTM ## 학습모델
import Word2Vec as Word2Vec ## 벡터화 모델
import gensim ## 벡터화 모듈
import numpy as np  ## 벡터((리스트)모듈)
import os  ## 벡터((리스트)모듈)
## 작업 디렉토리 지정
os.chdir('E:\\senier_project\\run\\Data\\')## 현재 실행하는 스크립트 경로 변경

def Convert2Vec(model_name, sentence):
    word_vec = []
    sub = []
    model = gensim.models.word2vec.Word2Vec.load(model_name)
    for word in sentence:
        if (word in model.wv.vocab):
            sub.append(model.wv[word])
        else:
            sub.append(np.random.uniform(-0.25, 0.25, 300))  # used for OOV words
    word_vec.append(sub)
    return word_vec

def Grade(sentence):
    tokens = W2V.tokenize(sentence)
    embedding = Convert2Vec('post.embedding', tokens)
    zero_pad = W2V.Zero_padding(embedding, Batch_size, Maxseq_length, Vector_size)
    global sess
    result = sess.run(prediction, feed_dict={X: zero_pad, seq_len: [len(tokens)]}) # tf.argmax(prediction, 1)이 여러 prediction 값중 max 값 1개만 가져옴
    point = result.ravel().tolist()
    ## ** 카테고리에 맞게 수정 ** ##
    Tag = ['body', 'comm', 'social', 'art', 'science']
    for t, i in zip(Tag, point):
        if len(t) <= 6:
            print(t, '\t\t', round(i * 100, 2), "%")
        else:
            print(t, '\t', round(i * 100, 2), "%")


W2V = Word2Vec.Word2Vec() 
Batch_size = 1
Vector_size = 300
Maxseq_length = 500  # Max length of training data
learning_rate = 0.001
lstm_units = 128
num_class = 5
keep_prob = 1.0
print('확인')
X = tf.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.placeholder(tf.int32, shape = [None])

BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)

with tf.variable_scope("loss", reuse = tf.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)

prediction = tf.nn.softmax(logits)  # softmax(활성화 함수)

saver = tf.train.Saver()
init = tf.global_variables_initializer()
## 학습시킨 모델이름
modelName = "Bi_LSTM.model"

sess = tf.Session()
sess.run(init)
saver.restore(sess, modelName)
s=''
##exit 입력시 종료 ##
while(True):
    try:
        s = input("문장을 입력하세요 : ")
        Grade(s)
    except:
        pass