# Loss Functions

This MD context will explain you Loss functions with minimal efforts.

## What’s A Loss Function?

At its core, a loss function is incredibly simple: it’s a method of evaluating how well your algorithm models your dataset. If your predictions are totally off, your loss function will output a higher number. If they’re pretty good, it’ll output a lower one. As you change pieces of your algorithm to try and improve your model, your loss function will tell you if you’re getting anywhere.

We can design our own basic loss function to further explain how it works. For each prediction that we make, our loss function will simply measure the absolute difference between our prediction and the actual value. In mathematical notation, it might look something **abs(y_predicted - y)**.

![Loss function](https://github.com/prashplus/Logic-Gates/blob/master/images/ymx%20graph%20loss%20fucntion.png)

## Different Types of Loss Functions

A lot of the loss functions that you see implemented in cutting edge Machine Learning today can get complex and confusing. Loss functions fall under four major category:

### Regressive loss functions

They are used in case of regressive problems, that is when the target variable is continuous. Most widely used regressive loss functions is Mean Square Error.
Other loss functions are:

1. Absolute error -  It measures the mean absolulte value of the element-wise difference between input.
2. Smooth Absolute Error - A smooth version of Abs Criterion.

### Classification loss functions

The output variable in classification problem is usually a probability value f(x), called the score for the input x. Generally, the magnitude of the score represents the confidence of our predictions. The target variable y, is a binary variable, 1 for true and -1 for false.

Most classification losses mainly aim to maximize the margine. Some classification algorithms are:

1. Binary Cross Entroy
2. Negative Log likelihood
3. Margin Classifier
4. Soft Margin Classifier

### Embedding loss functions

It deasl with problems where we have to measure whether two inputs are similar or dissimilar. Some examples are:

1. L1 Hinge error - Calculates the L1 distance between two inputs.
2. Cosine Error - Cosine distance between two inputs.

## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog [Nimbus](http://prashplus.blogspot.com) for more Tech Stuff
### http://www.prashplus.com