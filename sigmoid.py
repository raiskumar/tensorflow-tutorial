import numpy as np

"""
Sigmoid is used as Activation or Transfer function in Neural Network.
Used for the binary classification task.
Sigmoid function squashes really small and really large inputs.
"""


def sigmoid_arr(inputs):
    """
    Calculates the sigmoid for the given input array
    """
    sigmoid_scores = [1 / float(1 + np.exp(-x)) for x in inputs]
    return sigmoid_scores


def sigmoid(x):
    """
    Calculate sigmoid for a value
    """
    return 1 / (1 + np.exp(-x))


# Derivative of the sigmoid function
# Gradient of sigmoid is f'(h)=f(h)(1-f(h))
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


# Test
sigmoid_inputs = [2, 3, 5, 6]
print "Sigmoid Array Output :: {}".format(sigmoid_arr(sigmoid_inputs))
print "Sigmoid of a value :: {}".format(sigmoid(3))
print "Derivative of a Sigmoid of a value :: {}".format(sigmoid_prime(3))

