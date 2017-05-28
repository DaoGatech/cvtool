import model
import numpy as np
import pickle
import tensorflow as tf

def neural_net_image_input(image_shape):
    """
    Return a Tensor for a batch of image input
    : image_shape: Shape of the images
    : return: Tensor for image input.
    """
    return tf.placeholder(tf.float32, shape=(None, *image_shape), name="x")


def neural_net_label_input(n_classes):
    """
    Return a Tensor for a batch of label input
    : n_classes: Number of classes
    : return: Tensor for label input.
    """
    return  tf.placeholder(tf.float32, shape=(None, n_classes), name="y")


def neural_net_keep_prob_input():
    """
    Return a Tensor for keep probability
    : return: Tensor for keep probability.
    """
    return tf.placeholder(tf.float32, name="keep_prob")

def train_neural_network(session, optimizer, keep_probability, feature_batch, label_batch):
    """
    Optimize the session on a batch of images and labels
    : session: Current TensorFlow session
    : optimizer: TensorFlow optimizer function
    : keep_probability: keep probability
    : feature_batch: Batch of Numpy image data
    : label_batch: Batch of Numpy label data
    """
    feed_dict = {x : feature_batch, y : label_batch, keep_prob : keep_probability}
    session.run([optimizer], feed_dict=feed_dict)

def print_stats(session, features, labels, cost, accuracy):
    """
    Print information about loss and validation accuracy
    : session: Current TensorFlow session
    : features: Batch of Numpy image data
    : label_batch: Batch of Numpy label data
    : cost: TensorFlow cost function
    : accuracy: TensorFlow accuracy function
    """
    feed_dict = {x : features, y : labels, keep_prob : 1.0}
    _, l, acc = session.run([optimizer, cost, accuracy], feed_dict=feed_dict)
    print('loss: %f' % l)
    print('Accuracy: %.2f%%' % (acc*100.0))

def batch_features_labels(features, labels, batch_size):
    """
    Split features and labels into batches
    """
    for start in range(0, len(features), batch_size):
        end = min(start + batch_size, len(features))
        yield features[start:end], labels[start:end]

# Tune Parameters
epochs = 5
batch_size = 256
keep_probability = 0.5

# Model
with tf.variable_scope("convolutional"):
    x = neural_net_image_input((28, 28, 1))
    keep_prob = neural_net_keep_prob_input()
    logits, variables = model.conv_net(x, keep_prob)

# Inputs
y = neural_net_label_input(10)

# Name logits Tensor, so that is can be loaded from disk after training
logits = tf.identity(logits, name='logits')

# Loss and Optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
optimizer = tf.train.AdamOptimizer().minimize(cost)

# Accuracy
correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32), name='accuracy')

features, labels = pickle.load(open('train_data.p', mode='rb'))
valid_features, valid_labels = pickle.load(open('valid_data.p', mode='rb'))

save_model_path = './notMNIST_saved_model'
saver = tf.train.Saver(variables)
with tf.Session() as sess:
    # Initializing the variables
    sess.run(tf.global_variables_initializer())
    
	# Training cycle
    for epoch in range(epochs):
        for batch_features, batch_labels in batch_features_labels(features, labels, batch_size):
            train_neural_network(sess, optimizer, keep_probability, batch_features, batch_labels)
        print('Epoch {:>2}:  '.format(epoch + 1), end='')
        print_stats(sess, valid_features, valid_labels, cost, accuracy)

    save_path = saver.save(sess, save_model_path)