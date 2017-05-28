import tensorflow as tf

def conv2d_maxpool(x_tensor, conv_num_outputs, conv_ksize, conv_strides, pool_ksize, pool_strides):
    """
    Apply convolution then max pooling to x_tensor
    :param x_tensor: TensorFlow Tensor
    :param conv_num_outputs: Number of outputs for the convolutional layer
    :param conv_ksize: kernal size 2-D Tuple for the convolutional layer
    :param conv_strides: Stride 2-D Tuple for convolution
    :param pool_ksize: kernal size 2-D Tuple for pool
    :param pool_strides: Stride 2-D Tuple for pool
    : return: A tensor that represents convolution and max pooling of x_tensor
    """
    weight = tf.Variable(tf.truncated_normal([conv_ksize[0], conv_ksize[1], int(x_tensor.shape[3]), conv_num_outputs], stddev=0.1))
    bias = tf.Variable(tf.zeros([conv_num_outputs]))
    conv = tf.nn.conv2d(x_tensor, weight, strides=[1,conv_strides[0],conv_strides[1], 1], padding='SAME')
    relu = tf.nn.relu(conv + bias)
    return weight, bias, tf.nn.max_pool(relu, ksize=[1,pool_ksize[0],pool_ksize[1],1], strides=[1,pool_strides[0],pool_strides[1],1], padding='SAME')

def flatten(x_tensor):
    """
    Flatten x_tensor to (Batch Size, Flattened Image Size)
    : x_tensor: A tensor of size (Batch Size, ...), where ... are the image dimensions.
    : return: A tensor of size (Batch Size, Flattened Image Size).
    """
    shape = x_tensor.get_shape().as_list()
    return tf.reshape(x_tensor,[-1, shape[1]*shape[2]*shape[3]])


def fully_conn(x_tensor, num_outputs):
    """
    Apply a fully connected layer to x_tensor using weight and bias
    : x_tensor: A 2-D tensor where the first dimension is batch size.
    : num_outputs: The number of output that the new tensor should be.
    : return: A 2-D tensor where the second dimension is num_outputs.
    """
    weight = tf.Variable(tf.truncated_normal([x_tensor.get_shape().as_list()[1], num_outputs], stddev=0.1))
    bias = tf.Variable(tf.constant(1.0, shape=[num_outputs]))
    return weight, bias, tf.nn.relu(tf.add(tf.matmul(x_tensor, weight), bias))


def output(x_tensor, num_outputs):
    """
    Apply a output layer to x_tensor using weight and bias
    : x_tensor: A 2-D tensor where the first dimension is batch size.
    : num_outputs: The number of output that the new tensor should be.
    : return: A 2-D tensor where the second dimension is num_outputs.
    """
    weight = tf.Variable(tf.truncated_normal([x_tensor.get_shape().as_list()[1], num_outputs], stddev=0.1))
    bias = tf.Variable(tf.constant(1.0, shape=[num_outputs]))
    return weight, bias, tf.add(tf.matmul(x_tensor, weight), bias)

def conv_net(x, keep_prob):
    """
    Create a convolutional neural network model
    : x: Placeholder tensor that holds image data.
    : keep_prob: Placeholder tensor that hold dropout keep probability.
    : return: Tensor that represents logits
    """
    # Function Definition from Above:
    #    conv2d_maxpool(x_tensor, conv_num_outputs, conv_ksize, conv_strides, pool_ksize, pool_strides)
    w_conv1, b_conv1, conv = conv2d_maxpool(x, 24, (3,3), (1,1), (2,2), (2,2))
    w_conv2, b_conv2, conv = conv2d_maxpool(conv, 48, (3,3), (1,1), (2,2), (2,2))
    w_conv3, b_conv3, conv = conv2d_maxpool(conv, 128, (3,3), (1,1), (2,2), (2,2))

    flat = flatten(conv)

    # Function Definition from Above:
    #   fully_conn(x_tensor, num_outputs)
    w_fc1, b_fc1, full = fully_conn(flat, 512)
    drop = tf.nn.dropout(full,keep_prob)
    w_fc2, b_fc2, full = fully_conn(drop, 512)
    drop = tf.nn.dropout(full,keep_prob)

    # Function Definition from Above:
    #   output(x_tensor, num_outputs)
    w_out, b_out, logits = output(drop, 10)
    
    return logits, [w_conv1, b_conv1, w_conv2, b_conv2, w_conv3, b_conv3, w_fc1, b_fc1, w_fc2, b_fc2, w_out, b_out]

