# Logic Gates

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)

A logic gate is an idealized or physical device implementing a Boolean function; that is, it performs a logical operation on one or more binary inputs and produces a single binary output.
But, here this repository in not meant to tell you about logic gates but to tell you about Neural Networks by implementing logic gates using it.

This will not tell about working of different types of Neural networks but you will definitely become familier with the TFlearn and Keral. TFlearn and Keras are both widely popular higher level API built on the top of the Tensorflow. They are designed to reduce the complexity of the Tensorflow workflow while working with Machine Learning models.

If you are not familier with the Tensorflow then visit my repository: [ML](https://github.com/prashplus/ML).

Setup the prerequisites and start following the below steps.



## Keras

![keras](https://s3.amazonaws.com/keras.io/img/keras-logo-2018-large-1200.png)

Keras is a high-level neural networks API, written in Python and capable of running on top of **TensorFlow**, **CNTK**, or **Theano**. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

* Allows for easy and fast prototyping (through user friendliness, modularity, and extensibility).
* Supports both convolutional networks and recurrent networks, as well as combinations of the two.
* Runs seamlessly on CPU and GPU.

### Activation Functions

Just go through this brief intro the popular [Activation Functions](https://github.com/prashplus/Logic-Gates/blob/master/ACTIVATION.md). You will get all the required things to know before going through all the programs.
Or you can visit my blog at : [Activation Functions](http://prashplus.blogspot.com/2018/07/activation-functions-neural-networks.html)

### Loss Functions

The Loss Function is the bread and butter of modern Machine Learning. It takes your algorithm from theoretical to practical and transforms neural networks from glorified matrix multiplication into Deep Learning.

The choice of Optimisation Algorithms and Loss Functions for a Deep learning model can play a big role in producing optimum and faster results.

This [Loss function MD](https://github.com/prashplus/Logic-Gates/blob/master/LOSS.md) post will help you to quickly gain the usefull info if you are not much familier its importance in the Neural Networks.

### Model.Compile

In order for the neural network to be able to make the right adjustments to the weights we need to be able to tell how good our model is performing. Or to be more specific, with neural nets we always want to calculate a number that tells us how bad our model performs and then try to get that number lower.

That number is the so called loss and we can decide how the loss is calculated. Similar to how we picked **relu** as our activation function we picked **mean_squared_error** as our loss function simply because it’s a well proven loss function. We could change it to **binary_crossentropy** and our model would still continue to work. Again, we aren’t saying all loss functions can be used interchangeably. They do serve specific use cases. It’s just that we don’t have to understand all the heavy math behind each function to get going!

That brings us to the next parameter, the **optimizer**. The job of the optimizer is it to find the right adjustments for the weights. I’m sure by now you may guess how we picked adam as our optimizer of choice. Right, because it’s a well proven one!

The third parameter, **metrics** is actually much more interesting for our learning efforts. Here we can specify which metrics to collect during the training. We are interested in the binary_accuracy which gives us access to a number that tells us exactly how accurate our predictions are.


## TFLearn

![tflearn](https://avatars1.githubusercontent.com/u/16848261?s=280&v=4)

TFlearn is a modular and transparent deep learning library built on top of Tensorflow. It was designed to provide a higher-level API to TensorFlow in order to facilitate and speed-up experimentations, while remaining fully transparent and compatible with it.

TFLearn features include:

* Easy-to-use and understand high-level API for implementing deep neural networks, with tutorial and examples.
* Fast prototyping through highly modular built-in neural network layers, regularizers, optimizers, metrics...
* Full transparency over Tensorflow. All functions are built over tensors and can be used independently of TFLearn.
* Powerful helper functions to train any TensorFlow graph, with support of multiple inputs, outputs and optimizers.
* Easy and beautiful graph visualization, with details about weights, gradients, activations and more...
* Effortless device placement for using multiple CPU/GPU.

The high-level API currently supports most of recent deep learning models, such as Convolutions, LSTM, BiRNN, BatchNorm, PReLU, Residual networks, Generative networks... In the future, TFLearn is also intended to stay up-to-date with latest deep learning techniques.

## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog [Nimbus](http://prashplus.blogspot.com) for more Tech Stuff
### http://www.prashplus.com
