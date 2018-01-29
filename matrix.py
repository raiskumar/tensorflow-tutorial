import tensorflow as tf
import numpy as np

'''
A matrix concisely represents a list of vectors, where each column of a matrix is a feature vector.
A tensor is a generalization of a matrix that specifies an element by an arbitrary number of indices.
In general, the rank of a tensor is the number of indices required to specify an element.
'''

# Define a 2x2 matrix in 3 different ways

# list using python
m1 = [[1.0, 2.0],
      [3.0, 4.0]]

# ndarray from NumPy library
m2 = np.array([[1.0, 2.0],
               [3.0, 4.0]], dtype=np.float32)

# Tensorflow's tensor object
m3 = tf.constant([[1.0, 2.0],
                  [3.0, 4.0]])

# Print the type for each matrix
print(type(m1))  # <type 'list'>
print(type(m2))  # <type 'numpy.ndarray'>
print(type(m3))  # <class 'tensorflow.python.framework.ops.Tensor'>

# Create tensor objects out of the different types
t1 = tf.convert_to_tensor(m1, dtype=tf.float32)
t2 = tf.convert_to_tensor(m2, dtype=tf.float32)
t3 = tf.convert_to_tensor(m3, dtype=tf.float32)

# Now type of t1, t2 and t3 will be same
print(type(t1))
print(type(t2))
print(type(t3))

# Define an arbitrary matrix
matrix1 = tf.constant([[1, 2]])
matrix2 = tf.constant([[3, 4]])

neg_matrix = tf.negative(matrix1) # Run the negation operator on it
sum_matrix = tf.add(matrix1, matrix2) # sum two
mul_matrix = tf.multiply(matrix1, matrix2)

# Start a session to be able to run operations
with tf.Session() as sess:
    print "Negation=", sess.run(neg_matrix)
    print "Sum=", sess.run(sum_matrix)
    print "Mul=", sess.run(mul_matrix)


