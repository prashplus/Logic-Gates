# Optimisation Algorithms

Optimisation Algorithms are used to update weights and biases i,e. the internal parameters of a model to reduce the error. They can be divided into two categories:

### Constant Learning Rate Algorithms

Most widely used Optimisation Algorithm, the Stochastic Gradient Descent falls under this category.

![Opti](https://github.com/prashplus/Logic-Gates/blob/master/images/optimisation.gif)

Here η is called as learning rate which is a hyperparameter that has to be tuned. Choosing a proper learning rate can be difficult. A learning rate that is too small leads to painfully slow convergence i.e will result in small baby steps towards finding optimal parameter values which minimize loss and finding that valley which directly affects the overall training time which gets too large. While a learning rate that is too large can hinder convergence and cause the loss function to fluctuate around the minimum or even to diverge.

A similar hyperparameter is momentum, which determines the velocity with which learning rate has to be increased as we approach the minima.

### Adaptive Learning Algorithms

The challenge of using gradient descent is that their hyper parameters have to be defined in advance and they depend heavily on the type of model and problem. Another problem is that the same learning rate is applied to all parameter updates. If we have sparse data, we want to update the parameters in different extent instead.

Adaptive gradient descent algorithms such as Adagrad, Adadelta, RMScprop, Adam, provide an alternative to classical SGD. They have per-parameter learning rate methods, which provide heuristic approach without requiring expensive work in tuning hyperparameters for the learning rate schedule manually.

## Working with Optimisation Functions

### Stochastics Gradient Decent

Gradient Descent calcultes gradient for the whole dataset and updates values in direction opposite to the gradients until we find a local minima. Stochastic Gradient Descent performs a parameter update for each training example unlike normal Gradient Descent which performs only one update. Thus it is much faster. Gradient Decent algorithms can further be improved by tuning important parametes like momentum, learning rate etc.

### Adagrad

It is more preferrable for a sparse data set as it makes big updates for infrequent parameters and small updates for frequent parameters. It uses a different learning Rate for every parameter θ at a time step based on the past gradients which were computed for that parameter. Thus we do not need to manually tune the learning rate.

### Adam

It stands for Adaptive Moment Estimation. It also calculates different learning rate. Adam works well in practice, is faster, and outperforms other techniques.

**Stochastic Gradient Decent was much faster than the other algorithms but the results produced were far from optimum. Both, Adagrad and Adam produced better results that SGD, but they were computationally extensive. Adam was slightly faster than Adagrad. Thus, while using a particular optimization function, one has to make a trade off between more computation power and more optimum results.**

### Referred from :
1. https://medium.com/data-science-group-iitr/loss-functions-and-optimization-algorithms-demystified-bb92daff331c

2. https://blog.algorithmia.com/introduction-to-loss-functions/

## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog [Nimbus](http://prashplus.blogspot.com) for more Tech Stuff
### http://www.prashplus.com