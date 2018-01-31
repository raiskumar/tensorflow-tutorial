import tensorflow as tf

'''
Variables in TensorFlow are in-memory buffers containing tensors 
which have to be explicitly initialized and used in-graph to maintain state across session. 
Just like normal python variables which can be modified.
'''

x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')   # y = x + 5

# Initialization of the variables must be run before all other operations in the model.i
model = tf.global_variables_initializer()

# model =tf.variables_initializer(var_list=[y])     # 2nd approach

with tf.Session() as session:
    session.run(model)
    print(session.run(y))
    y = y + 1
    print(session.run(y))
