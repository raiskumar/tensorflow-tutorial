import tensorflow as tf

'''
Variables in TensorFlow are in-memory buffers containing tensors 
which have to be explicitly initialized and used in-graph to maintain state across session. 
'''

x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')   # y = x + 5

# Initialize all the variables;
model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))
    y = y + 1
    print(session.run(y))

