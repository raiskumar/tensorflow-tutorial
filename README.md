### TensorFlow

A library for DATAFLOW Programming or massive array manipulation.

Tensorflow works by first defining and describing our model in abstract, and then, when we are ready we make it reallity using session. The description of the model is known as *Computational Graph* in Tensorflow.  In the Computation Graph, the execution is NOT performed, though it looks so. In fact, event the variables are not initialized. 

##### So, it has two phases:
1. Construction Phase
2. Execution Phase

### Tensor
In Tensorflow, data like integer, float, and Strings are not handled like other programming languages. These values get encapsulated into an object called as Tensor. 

`
hello = tf.constant('Hello, TensorFlow')
`

Above is a 0-dimenstion String tensor and it's constant so its value will never change. 

### Session
As discussed above, TensorFlow has two phases. In second phase the tensor's get evaluated using Session. So, it's basically environment for running a graph. It's also in charge of allocating the graph to GPU or CPU for evalution. 



