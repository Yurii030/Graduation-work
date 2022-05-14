## 학습 모델
import tensorflow as tf

class Bi_LSTM():
    
    def __init__(self, lstm_units, num_class, keep_prob):
        ## litm_units 변수 (128)
        self.lstm_units = lstm_units
        
        with tf.compat.v1.variable_scope('forward', reuse = tf.compat.v1.AUTO_REUSE): 
        ## get_variable() 에서 생성된 변수를 관리 (해당 함수는 forward 변수를 관리)
            self.lstm_fw_cell = tf.nn.rnn_cell.LSTMCell(lstm_units, forget_bias=1.0, state_is_tuple=True)
            self.lstm_fw_cell = tf.contrib.rnn.DropoutWrapper(self.lstm_fw_cell, output_keep_prob = keep_prob)
            
        with tf.compat.v1.variable_scope('backward', reuse = tf.compat.v1.AUTO_REUSE):
            
            self.lstm_bw_cell = tf.nn.rnn_cell.LSTMCell(lstm_units, forget_bias=1.0, state_is_tuple=True)
            self.lstm_bw_cell = tf.contrib.rnn.DropoutWrapper(self.lstm_fw_cell, output_keep_prob = keep_prob)
        
        with tf.compat.v1.variable_scope('Weights', reuse = tf.compat.v1.AUTO_REUSE):
        
            self.W = tf.compat.v1.get_variable(name="W_2", shape=[2 * lstm_units, num_class],
                                dtype=tf.float32, initializer=tf.contrib.layers.xavier_initializer())
            self.b = tf.compat.v1.get_variable(name="b", shape=[num_class], dtype=tf.float32,
                                initializer=tf.zeros_initializer())
            
            
    def logits(self, X, W, b, seq_len):
        
        (output_fw, output_bw), states = tf.nn.bidirectional_dynamic_rnn(self.lstm_fw_cell, self.lstm_bw_cell,dtype=tf.float32,
                                                                            inputs = X, sequence_length = seq_len)
        ## concat fw, bw final states
        outputs = tf.concat([states[0][1], states[1][1]], axis=1)
        pred = tf.matmul(outputs, W) + b        
        return pred
        
    def model_build(self, logits, labels, learning_rate = 0.001):
        
        with tf.compat.v1.variable_scope("loss"):
            
            loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits = logits , labels = labels)) # Softmax loss
            optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss) # Adam Optimizer
            
        return loss, optimizer
    
    def graph_build(self, avg_loss, avg_acc):
        
        tf.compat.v1.summary.scalar('Loss', avg_loss)
        tf.compat.v1.summary.scalar('Accuracy', avg_acc)
        merged = tf.compat.v1.summary.merge_all()
        return merged
