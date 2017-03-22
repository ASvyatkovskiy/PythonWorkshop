import os
import tensorflow as tf

LOGDIR = '/tmp/mnist_tutorial/'

### MNIST EMBEDDINGS ###
mnist = tf.contrib.learn.datasets.mnist.read_data_sets(train_dir=LOGDIR + 'data', one_hot=True)

def conv_layer(input, size_in, size_out):
    w = tf.Variable(tf.zeros([5, 5, size_in, size_out]))
    b = tf.Variable(tf.zeros([size_out]))
    conv = tf.nn.conv2d(input, w, strides=[1, 1, 1, 1], padding="SAME")
    act = tf.nn.relu(conv + b)
    return tf.nn.max_pool(act, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")


def fc_layer(input, size_in, size_out):
    w = tf.Variable(tf.zeros([size_in, size_out]))
    b = tf.Variable(tf.zeros([size_out]))
    act = tf.nn.relu(tf.matmul(input, w) + b)
    return act


def mnist_model(learning_rate, subfolder):
  tf.reset_default_graph()
  sess = tf.Session()

  # Setup placeholders, and reshape the data
  x = tf.placeholder(tf.float32, shape=[None, 784])
  x_image = tf.reshape(x, [-1, 28, 28, 1])
  tf.summary.image('input', x_image, 3)
  y = tf.placeholder(tf.float32, shape=[None, 10])

  #Convolutional layers
  conv1 = conv_layer(x_image, 1, 32)
  conv_out = conv_layer(conv1, 32, 64)

  flattened = tf.reshape(conv_out, [-1, 7 * 7 * 64])

  #Fully connected layers
  fc1 = fc_layer(flattened, 7 * 7 * 64, 1024)
  logits = fc_layer(fc1, 1024, 10)

  #Calculate crossentropy
  xent = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(
            logits=logits, labels=y))

  #Set up optimizer
  train_step = tf.train.AdamOptimizer(learning_rate).minimize(xent)

  correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  summ = tf.summary.merge_all()

  saver = tf.train.Saver()

  sess.run(tf.global_variables_initializer())
  writer = tf.summary.FileWriter(LOGDIR + subfolder)
  writer.add_graph(sess.graph)

  for i in range(201):
    print "Run epoch {}".format(i)
    batch = mnist.train.next_batch(100)
    if i % 5 == 0:
      [train_accuracy, s] = sess.run([accuracy, summ], feed_dict={x: batch[0], y: batch[1]})
      writer.add_summary(s, i)
    if i % 50 == 0:
      saver.save(sess, os.path.join(LOGDIR, "model.ckpt"), i)
    sess.run(train_step, feed_dict={x: batch[0], y: batch[1]})


def main(subfolder):
  learning_rate = 1E-4
  mnist_model(learning_rate, subfolder)


if __name__ == '__main__':
  subfolder = "0"
  main(subfolder)
