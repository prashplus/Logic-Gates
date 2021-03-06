import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

# Define Training DATA i.e, AND Gate Inputs
input = np.array([[0,0],[0,1],[1,0],[1,1]])
output = np.array([[0],[0],[0],[1]])

# Model Definition
model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',optimizer='adam', metrics=['binary_accuracy'])

# Train Model
model.fit(input, output, nb_epoch=600, verbose=2)

# Validation
print("Round off Values: \n",model.predict(input).round())
print("Actual Values: \n",model.predict(input))