import numpy as np
data = np.loadtxt('Smarket.csv', skiprows=1, delimiter=',', usecols=(1,6))
datastr = np.loadtxt('Smarket.csv', skiprows=1, delimiter=',', usecols=(8), dtype='str')

datastr[ datastr=='Up' ] = 1 #convert up/down to 1/0 respectively, for sake of binary logistic regression
datastr[ datastr=='Down' ] = 0
X = np.hstack( (np.ones((1250,1)), data[:,:]))
Y = np.array(datastr, dtype='float')

Beta_old = [0, 0, 0] #doing Newton's method by hand, as outlined in "The Elements of Statistical Learning"
for c in range(10):
    P = np.exp(X@Beta_old)/(1+np.exp(X@Beta_old))
    W_1 = P*(1-P)
    W_2 = np.expand_dims(W_1, axis=1)
    W = np.diag( np.squeeze( W_2 ) )
    Beta_new = Beta_old + np.linalg.inv(X.T@W@X)@X.T@(Y-P.T)
    Beta_old = Beta_new
print(Beta_new)

probs = np.ones(1250)
for i in range(1250):
    prob = np.exp(X[i,:]@Beta_new)/(1+np.exp(X[i,:]@Beta_new))
    if prob<0.5:
        probs[i] = 0

probability = np.expand_dims(probs, axis=1)
np.savetxt("probs_manual.csv", probability, delimiter=",", fmt='%i')
