# Activation Functions

Activation functions are really important for a Neural Network to learn and make sense of something really complicated and Non-linear complex functional mappings between the inputs and response variable.They introduce non-linear properties to our Network.Their main purpose is to convert a input signal of a node in a A-NN to an output signal. That output signal now is used as a input in the next layer in the stack.

Specifically in A-NN we do the sum of products of **inputs(X)** and their corresponding **Weights(W)** and apply a **Activation function f(x)** to it to get the output of that layer and feed it as an input to the next layer.

In keras, we can use different activation function for each layer. That means that in our case we have to decide what activation function we should be utilized in the hidden layer and the output layer.

Activations can either be used through an Activation layer, or through the activation argument supported by all forward layers:

![Neuron](https://cdn-images-1.medium.com/max/1000/1*vGj29ZBD1kH1kDlGQspPxA.png)

### “Input times weights , add Bias and Activate”

```python
from keras.layers import Activation, Dense

model.add(Dense(64))
model.add(Activation('tanh'))
```

This is equivalent to:

```python
model.add(Dense(64, activation='tanh'))
```

You can also pass an element-wise TensorFlow/Theano/CNTK function as an activation:

```python
model.add(Dense(64, activation=K.tanh))
```


## Step Function

![step function](https://cdn-images-1.medium.com/max/1000/0*8U8_aa9hMsGmzMY2.)

Activation function A = “activated” if Y > threshold else not

### Pros

* Simple to understand

### Cons

* Can't handle multiple classes.
* Can't give output like 20% or 30%.

### Conclusion

Give other activation function for the hidden layers and you can use step function in the final layer.

## Linear Function

A straight line function where activation is proportional to input ( which is the weighted sum from neuron ).

### Pros

* It gives a range of activations, so it is not binary activation.
* We can definitely connect a few neurons together and if more than 1 fires, we could take the max ( or softmax) and decide based on that.

### Cons

* For this function, derivative is a constant. That means, the gradient has no relationship with X.
* It is a constant gradient and the descent is going to be on constant gradient.
* If there is an error in prediction, the changes made by back propagation is constant and not depending on the change in input delta(x) !

## Sigmoid Function

![Sigmoid function](https://cdn-images-1.medium.com/max/1000/0*5euYS7InCmDP08ir.)

It is a activation function of form f(x) = 1 / 1 + exp(-x) . Its Range is between 0 and 1. It is a S — shaped curve.

### Pros

* It is nonlinear in nature. Combinations of this function are also nonlinear!
* It will give an analog activation unlike step function.
* It has a smooth gradient too.
* It’s good for a classifier.
* The output of the activation function is always going to be in range (0,1) compared to (-inf, inf) of linear function. So we have our activations bound in a range. Nice, it won’t blow up the activations then.

### Cons

* Towards either end of the sigmoid function, the Y values tend to respond very less to changes in X.
* It gives rise to a problem of “vanishing gradients”.
* Its output isn’t zero centered. It makes the gradient updates go too far in different directions. 0 < output < 1, and it makes optimization harder.
* Sigmoids saturate and kill gradients.
* The network refuses to learn further or is drastically slow ( depending on use case and until gradient /computation gets hit by floating point value limits ).

## Tanh (Hyperbolic Tangent function)

![tanh](https://cdn-images-1.medium.com/max/1000/0*YJ27cYXmTAUFZc9Z.)

A better version of Sigmoid for many cases due to its range.

![tanh2](https://cdn-images-1.medium.com/max/1000/1*U-677uRd-StXbAgrAnX2hw.png)

It’s mathamatical formula is f(x) = 1 — exp(-2x) / 1 + exp(-2x). Now it’s output is zero centered because its range in between -1 to 1 i.e -1 < output < 1 . Hence optimization is easier in this method hence in practice it is always preferred over Sigmoid function . But it still suffers from **Vanishing gradient problem**.

Deciding between the sigmoid or tanh will depend on your requirement of gradient strength.

### Pros

* The gradient is stronger for tanh than sigmoid ( derivatives are steeper).

### Cons

* Tanh also has the vanishing gradient problem.

## ReLu (Rectified Linear units)

It has become very popular in the past couple of years. It was recently proved that it had 6 times improvement in convergence from Tanh function. It’s just R(x) = max(0,x) i.e if x < 0 , R(x) = 0 and if x >= 0 , R(x) = x.

![RELU](https://cdn-images-1.medium.com/max/1000/0*qtfLu9rmtNullrVC.png)

### Pros

* It avoids and rectifies vanishing gradient problem.
* ReLu is less computationally expensive than tanh and sigmoid because it involves simpler mathematical operations.

### Cons

* One of its limitation is that it should only be used within Hidden layers of a Neural Network Model.

* Some gradients can be fragile during training and can die. It can cause a weight update which will makes it never activate on any data point again. Simply saying that ReLu could result in Dead Neurons.

* In another words, For activations in the region (x<0) of ReLu, gradient will be 0 because of which the weights will not get adjusted during descent. That means, those neurons which go into that state will stop responding to variations in error/ input ( simply because gradient is 0, nothing changes ). This is called dying ReLu problem.

* The range of ReLu is [0, inf). This means it can blow up the activation.


There are variations in ReLu to mitigate the issue of **Dying ReLU** issue by simply making the horizontal line into non-horizontal component . for example y = 0.01x for x<0 will make it a slightly inclined line rather than horizontal line. This is **Leaky ReLu**. There are other variations too. The main idea is to let the gradient be non zero and recover during training eventually.