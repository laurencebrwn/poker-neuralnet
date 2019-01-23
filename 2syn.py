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
w0 = 2*np.random.random((1,4)) - 1
w1 = 2*np.random.random((4,1)) - 1
#train
for t in xrange(100000):
    
    #forward propagation
    l0 = x
    l1 = sigma(np.dot(l0, w0))
    l2 = sigma(np.dot(l1, w1))
    
    #error + change calc
    l2_error = y - l2       
    l2_change = l2_error*sigma_deriv(l2)
    l1_error = l2_change.dot(w1.T)
    l1_change = l1_error * sigma_deriv(l1)
    
    #update weights
    w1 += np.dot(l1.T, l2_change)
    w0 += np.dot(l0.T, l1_change)
    
print "Output after training"
print l2

#user entry
c = raw_input("Card: ")
C = np.array(([[c]]), dtype=float)

#normalise
C = C/12

print sigma(np.dot(sigma(np.dot(C, w0)), w1))