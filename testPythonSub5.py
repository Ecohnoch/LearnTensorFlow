import tensorflow as tf 

def add_layer(inputs, in_size, out_size, activation_function = None):
	Weight = tf.Variable(tf.random_normal([in_size, out_size]))
	biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
	Wx_plus_b = tf.matmul(inputs, Weight) + biases
	if activation_function is None:
		output = Wx_plus_b
	else:
		output = activation_function(Wx_plus_b)
	return output

	