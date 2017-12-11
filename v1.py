import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras import optimizers
import random

model.fit(x_training, y_training, epochs=10, batch_size=32)


#(hcp, ace, king, queen, jack (spades, hearts, diamonds, clubs), length, 1,2,3,4,5,6)

#defining the datasets

'''
nht (north_hand_train)	#each data vector is 27 dimensions (hcp + 16 face cards + 4 suit lengths + 6 for bids made)
sht (south_hand_train)	#each data vector is 27 dimensions (hcp + 16 face cards + 4 suit lengths + 6 for bids made)
'''


def bandit(someinputarray, epsilon):
	l = random.uniform(0,1)
	if (l>epsilon):
		output max(someinputarray)
	else:
		probable = random.choice(someinputarray)
		if (probable != max(someinputarray)):
			output probable
		else:
			break

def update(hand, list_one, list_two):
	for i in range (0, 27):
		if (list_one[i] = 0):
			list_one[i] = hand
			list_two[i] = hand

	output (list_one, list_two)


#defining the model

model = Sequential()
model.add(Dense(128, activation='relu', input_dim=27))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

#now we have to take the output of each state and pass it to the bandit, 'tweak' the data with the bidding sequence the bandit gives and then train

create = []
for row in inputnumpyarray:
	prediction = model.predict(row)	#prediction is a numpy array
	hand = bandit(prediction, epsilon)	
	create = create.append(update(hand, nht, sht))	#update changes the entries (nht, sht will all have to be modulo 6)


model.fit(create, scoring , epochs=whatever, batch_size=32)
score = model.evaluate(...)



















