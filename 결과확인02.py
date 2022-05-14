"""
머신러닝을 마치고 최종적으로 문장을 입력하여 카테고리 유사도 확인
"""
## ** PART 3 . 학습이 완료된 모델을 통해 문장 입력시 카테고리별 유사도 출력 ** ##
##import import_ipynb         ## ipynb(주피터 노트북) 파일 임포트를 위한 모듈
import os                   ## 작업 디렉토리 지정을 위한 모듈
import tensorflow as tf     ## 머신러닝을 위한 모듈
import Bi_LSTM as Bi_LSTM   ## 학습 모델
import Word2Vec as Word2Vec ## 벡터화 모듈
import gensim               ## 벡터화 모듈
import numpy as np          ## 벡터(리스트) 모듈
## 작업 디렉토리 지정
os.chdir('C:\\anaconda\\morpy\\Bi_LSTM\\data\\')

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
    full = []
    cname = []
    pnuml = []
    
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
            
    """
        pNum = round(i * 100, 2)
        percent = t + str(round(i * 100, 2)) + "%"
        cname.append(t)
        pnuml.append(pNum)
        
        full.append(percent)
     maxnum = max(pnuml)
    cindex = 0
    cindex = pnuml.index(maxnum)
    print(cindex)
        
    
    return full, cname[cindex]
    """
    
W2V = Word2Vec.Word2Vec()

Batch_size = 1
Vector_size = 300
Maxseq_length = 500  # Max length of training data
learning_rate = 0.001
lstm_units = 128
## ** 카테고리에 개수 ** ##
num_class = 5
keep_prob = 1.0

X = tf.compat.v1.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.compat.v1.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.compat.v1.placeholder(tf.int32, shape = [None])

BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)

with tf.compat.v1.variable_scope("loss", reuse = tf.compat.v1.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)

prediction = tf.nn.softmax(logits)  # softmax

saver = tf.compat.v1.train.Saver()
init = tf.compat.v1.global_variables_initializer()
## 학습시킨 모델의 이름 ##
modelName = "Bi_LSTM.model"

sess = tf.Session()
sess.run(init)
## 모델을 불러옴 ##
saver.restore(sess, modelName)
s = ''
## exit 입력시 종료 ##
while(s != 'exit'):
    print('')
    print('exit 입력을 통해 종료')
    s = input('문장을 입력하세요 : ')
    if s == 'exit':
        break
    Grade(s)