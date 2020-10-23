import numpy as np
from sklearn.linear_model import LogisticRegression
data = np.loadtxt('Smarket.csv', skiprows=1, delimiter=',', usecols=(1,6))
datastr = np.loadtxt('Smarket.csv', skiprows=1, delimiter=',', usecols=(8), dtype='str')

datastr[ datastr=='Up' ] = 1 #convert up/down to 1/0 respectively, for sake of binary logistic regression
datastr[ datastr=='Down' ] = 0
X = data
Y = np.array(datastr, dtype='float')

model = LogisticRegression(solver='newton-cg', penalty='none') #create binary logistic regression model
model.fit(X,Y)

probs = model.predict(X[:,:]) #classify each datapoint as either 1/0. 1 corresponds with >50% chance of 'Up', 0 corresponds with <50% chance of 'Up'

probability = np.expand_dims(probs, axis=1) # making it into a nice csv
np.savetxt("probs.csv", probability, delimiter=",", fmt='%i')

print(model.intercept_, model.coef_)
