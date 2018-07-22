import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

# Define Training DATA i.e, Or Gate Inputs
input = np.array([[1],[0]])
output = np.array([[0],[1]])

# Model Definition
model = Sequential()
model.add(Dense(16, input_dim=1, activation='linear'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error',optimizer='adam', metrics=['binary_accuracy'])

# Train Model
model.fit(input, output, nb_epoch=100, verbose=2)

# Validation
print("Round off Values: \n",model.predict(input).round())
print("Actual Values: \n",model.predict(input))