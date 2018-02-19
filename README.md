### TensorFlow

A library for DATAFLOW Programming or massive array manipulation.

Tensorflow works by first defining and describing our model in abstract, and then, when we are ready, we make it reallity using session. The description of the model is known as *Computational Graph* in Tensorflow.  In the Computation Graph, the execution is NOT performed, though it looks so. *In fact, event the variables are not initialized.* 

##### So, it has two phases:
1. Construction Phase
2. Execution Phase

### Tensor
In TensorFlow, data like integers, floats, and Strings are not handled like other programming languages. These values get encapsulated into an object known as Tensors. 

`
hello = tf.constant('Hello, TensorFlow')
`

Above is a 0-dimenstion String tensor and it's constant so its value will never change. 

### Session
As discussed above, TensorFlow has two phases. In second phase the tensors get evaluated using Session. So, Session is basically an environment for running a graph. It's also in charge of allocating the graph to GPU or CPU for evalution. 

```
hello = tf.constant('Hello, TensorFlow')

with tf.Session() as session:
    result = session.run(hello)
    print result
```

Above snippet will print *Hello, TensorFlow*.
Session.run() method evaluates the session and then returns the result. 

### Feeding Data
Constant tensor values can't be change. Let's cover how can we feed data into TensorFlow. 

tf.placeholder() returns a tensor that gets its value from data passed to the tf.session.run() function, allowing you to set the input right before the session runs.

```
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
```

The above example shows the tensor x being set to the string "Hello, world" in the run method. Use the feed_dict parameter in tf.session.run() to set the placeholder tensor.

