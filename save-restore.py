import tensorflow as tf

"""
Demos how to save and restore the model.
 
Training the Neural Network takes quite long time to evolve your weights and biases. But, once you close your TensorFlow
session, you loose all that. To reuse the model you will have to re-train your models. 
Luckily, TensorFlow gives option to persist state of your model and then restore it later.
"""


def save():
    """
    This function will create below files on TensorFlow version 1.4.1
    1. model1.ckpt.data-*
    2. model1.ckpt.index
    3. model1.ckpt.meta

    """

    # .ckpt - checkpoint
    model_file = './model1.ckpt'

    # initialize with random values
    weights = tf.Variable(tf.truncated_normal([2, 3]))

    # Class used to save and/or restore Tensor Variables
    saver = tf.train.Saver()

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        print('Weights:')
        print session.run(weights)

        # Save the model
        saver.save(session, model_file)


def load():
    """
    This method restores the value of weight which was saved in save() method.
    Will be handy to persist the state of your hours of training
    """

    model_file = './model1.ckpt'

    # Remove the previous weights and bias
    tf.reset_default_graph()

    weights = tf.Variable(tf.truncated_normal([2, 3]))

    # Class used to save and/or restore Tensor Variables
    saver = tf.train.Saver()

    with tf.Session() as session:

        # Not Required; Below method sets the variables
        #session.run(tf.global_variables_initializer())

        # Load the weights and bias
        saver.restore(session, model_file)

        # Show the values of weights
        print('Restored Weights:')
        print(session.run(weights))


save()
load()
