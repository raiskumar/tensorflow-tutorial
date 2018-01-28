import tensorflow as tf
import random as ran


def sum_two_constants():
    '''
    Sum two random numbers using tensorflow
    '''

    a = tf.constant(ran.random())
    b = tf.constant(ran.random())

    # a and b are not normal variables but tensors; so plain a+b will NOT work
    sum = tf.add(a, b)

    with tf.Session() as session:
        print "Values are: ", session.run(a), "& ", session.run(b)
        return session.run(sum)


print sum_two_constants()  # Calculate sum of two constants


def sum_two_numbers(one, two):
    '''
    Sum two numbers; numbers are not constants and not provided in advance
    '''

    # inject data into the computation graph through placeholders
    a = tf.placeholder(tf.int32, name="a")
    b = tf.placeholder(dtype=tf.int32)  # name is optional
    sum = tf.add(a, b)

    with tf.Session() as session:
        return session.run(sum, feed_dict={a: one, b: two})


print sum_two_numbers(1, 2)
print sum_two_numbers(4, 6)

