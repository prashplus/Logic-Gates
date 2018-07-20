# Solving OR with 2x2x1 feed forward Neural Network
# including all the required dependencies

from tflearn import DNN
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

# Defining all the input data X and Y List
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [[0],[1],[1],[1]]

# Defining the Model or Neural Network
input_layer = input_data(shape=[None, 2])
hidden_layer = fully_connected(input_layer, 2 , activation='tanh')
output_layer = fully_connected(hidden_layer, 1, activation='tanh')

# Regressor that will perform backpropogation and train our network
regression = regression(output_layer, optimizer = 'sgd', loss = 'binary_crossentropy', learning_rate=5)
model = DNN(regression)

# And finally Training of the model
model.fit(X,Y, n_epoch=5000,show_metric=True)

# Model Insights
print(model.get_weights(hidden_layer.W), model.get_weights(hidden_layer.b))
print(model.get_weights(output_layer.W), model.get_weights(output_layer.b))

# Prediction examples
print ('Expected:  ', [i[0] > 0 for i in Y])
print ('Predicted: ', [i[0] > 0 for i in model.predict(X)])