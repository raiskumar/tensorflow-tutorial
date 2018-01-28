import tensorflow as tf

# Print the library version number
print "TensorFlow Version=", tf.__version__

# If you need constants with specific values inside your training model, then the constant object can be used
helloWorld = tf.constant("Hello, TensorFlow!", name="helloWorld", dtype=tf.string)  # node

'''
To actually evaluate the above node, we need to run computational graph with Session.
Session encapsulates the control and state of the Tensorflow runtime
'''

# Approach 1
session = tf.Session()
print session.run(helloWorld)
session.close()    # mandatory; to free up resources


# Approach 2
with tf.Session() as session:
    print session.run(helloWorld)  # session gets closed automatically


