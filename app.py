from flask import Flask, jsonify, render_template, request
import tensorflow as tf
import json
from ai import model
import numpy as np
#import pickle

app = Flask(__name__)

save_model_path = './ai/notMNIST_saved_model'
loaded_graph = tf.Graph()

x = tf.placeholder(tf.float32, shape=(None, 28, 28, 1))
sess = tf.Session()

with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder(tf.float32)
    logits, variables = model.conv_net(x, keep_prob)

saver = tf.train.Saver(variables)
saver.restore(sess, save_model_path)

@app.route("/")
def home():
	return render_template("home.html")

@app.route('/canvas', methods=['POST'])
def canvas():
	input = request.json['data']
	#pickle.dump(input, open('data.p', 'wb'))
	image = np.array(input) / 255.0
	image = image.reshape(1,28,28,1)
	result = predict(image)
	result = np.argmax(result)
	return jsonify(result=str(result))

def predict(input):
    return sess.run([logits], feed_dict={x: input, keep_prob: 1.0})[0][0]

if __name__ == '__main__':
    app.run()
