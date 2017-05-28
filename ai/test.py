import model
import numpy as np
import pickle
import tensorflow as tf

save_model_path = './notMNIST_saved_model'
loaded_graph = tf.Graph()

x = tf.placeholder(tf.float32, shape=(None, 28, 28, 1))
sess = tf.Session()

with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder(tf.float32)
    logits, variables = model.conv_net(x, keep_prob)

saver = tf.train.Saver(variables)
saver.restore(sess, save_model_path)

def predict(input):
    return sess.run([logits], feed_dict={x: input, keep_prob: 1.0})

#valid_features, valid_labels = pickle.load(open('./valid_data.p', mode='rb'))
#image = valid_features[0:10]

data = pickle.load(open('../data.p', mode='rb'))

image = np.array(data) / 255.0
image = image.reshape(1,28,28,1)

#print(image[:100])

print(predict(image))