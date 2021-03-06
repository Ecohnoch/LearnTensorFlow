import tensorflow as tf 
import numpy as np 

# creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

### creat tensorflow struture start
Weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weight * x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

### creat tensorflow structure end

sess = tf.Session()
sess.run(init)  # Very important

for step in range(201):
    sess.run(train)
    print(step, sess.run(Weight), sess.run(biases))

