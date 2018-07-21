# Logic Gates

A logic gate is an idealized or physical device implementing a Boolean function; that is, it performs a logical operation on one or more binary inputs and produces a single binary output.
But, here this repository in not meant to tell you about logic gates but to tell you about Neural Networks by implementing logic gates using it.

This will not tell about working of different types of Neural networks but you will definitely become familier with the TFlearn and Keral. TFlearn and Keras are both widely popular higher level API built on the top of the Tensorflow. They are designed to reduce the complexity of the Tensorflow workflow while working with Machine Learning models.

If you are not familier with the Tensorflow then visit my repository: [ML](https://github.com/prashplus/ML).

Setup the prerequisites and start following the below steps.


## Keras

### Model.Compile

In order for the neural network to be able to make the right adjustments to the weights we need to be able to tell how good our model is performing. Or to be more specific, with neural nets we always want to calculate a number that tells us how bad our model performs and then try to get that number lower.

That number is the so called loss and we can decide how the loss is calculated. Similar to how we picked **relu** as our activation function we picked **mean_squared_error** as our loss function simply because it’s a well proven loss function. We could change it to **binary_crossentropy** and our model would still continue to work. Again, we aren’t saying all loss functions can be used interchangeably. They do serve specific use cases. It’s just that we don’t have to understand all the heavy math behind each function to get going!

That brings us to the next parameter, the **optimizer**. The job of the optimizer is it to find the right adjustments for the weights. I’m sure by now you may guess how we picked adam as our optimizer of choice. Right, because it’s a well proven one!

The third parameter, **metrics** is actually much more interesting for our learning efforts. Here we can specify which metrics to collect during the training. We are interested in the binary_accuracy which gives us access to a number that tells us exactly how accurate our predictions are.

## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog [Nimbus](http://prashplus.blogspot.com) for more Tech Stuff
### http://www.prashplus.com