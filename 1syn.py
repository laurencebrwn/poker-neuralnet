import numpy as np  

#make sigma
def sigma(x):  
    return 1/(1+np.exp(-x))

#sigma gradient
def sigma_deriv(x):
    return x*(1-x)

#define datasets
x = np.array(([[0],[12],[4],[7]]), dtype=float)
y = np.array([[1],[0],[1],[0]])

#normalise
x = x/12

#seed
np.random.seed(1)

#weights
w = 2*np.random.random((1,1)) - 1

#train
for t in xrange(100000):
	#forward propogation
	l0 = x
	l1 = sigma(np.dot(l0, w))

	#error calc
	l1_error = y - l1

	#change calc
	l1_change = l1_error*sigma_deriv(l1)

	#update weights
	w += np.dot(l0.T,l1_change)

print "Output after training"
print l1