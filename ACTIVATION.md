# Activation

In keras, we can use different activation function for each layer. That means that in our case we have to decide what activation function we should be utilized in the hidden layer and the output layer.

Activations can either be used through an Activation layer, or through the activation argument supported by all forward layers:

![Neuron](https://cdn-images-1.medium.com/max/1000/1*vGj29ZBD1kH1kDlGQspPxA.png)


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