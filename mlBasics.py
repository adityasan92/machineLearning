import tensorflow as tf

# x = tf.placeholder(tf.float32, [None, 784])

# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))

# y = tf.nn.softmax(tf.matmul(x, W) + b)

# y_ = tf.placeholder(tf.float32, [None, 10])

# cross_entropy = -tf.reduce_sum(y_*tf.log(y))
# train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)