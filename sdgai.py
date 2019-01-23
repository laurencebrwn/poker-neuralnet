import numpy as np
import csv, random, itertools
from random import randint

class sdg_nn:
	__action = ''

		#define datasets
	__x = np.genfromtxt('handstrained.csv', delimiter=',')
	__y = np.genfromtxt('correctpredtrained.csv', delimiter=',')[np.newaxis]
	__y = __y.T
	#seed
	np.random.seed(1)
	#weights
	__w0 = 2*np.random.random((3,4))-1
	__w1 = 2*np.random.random((4,4))-1
	__w2 = 2*np.random.random((4,4))-1
	__w3 = 2*np.random.random((4,1))-1
	#raise check
	__allReadyRaise = False
	
	__move = 0
	
	def setAction(self,card1,card2):
		self.__action = self.predict(card1,card2)
	def getAction(self):
		return self.__action

	def sigma(self,x):
		return 1/(1+np.exp(-x))
	#sigma gradient
	def sigmaDeriv(self,x):
		return x*(1-x)
	def predict(self,c01,c02):
		__carray = self.processCards(c01,c02)
		for i in xrange(10):
			self.epoch()
   		#predict
		__c1 = __carray[0]
		__c2 = __carray[1]
		__s = __carray[2]
		__C = np.array([[__c1,__c2,__s]])
		self.__move = self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(__C, self.__w0)), self.__w1)), self.__w2)), self.__w3))
		
		if self.__move >= 0.7 and self.__allReadyRaise == False: 
			self.__allReadyRaise = True
			return 'r'
		elif self.__move >=0.5: return 'c'
		else: return 'f'
	def epoch(self):
		__z=0
		#train
		for t in xrange(len(self.__y)/4):
			#forward propagation
			__l0 = self.__x[__z:(__z+5)]
  			__l1 = self.sigma(np.dot(__l0, self.__w0))
   			__l2 = self.sigma(np.dot(__l1, self.__w1))
  			__l3 = self.sigma(np.dot(__l2, self.__w2))
  			__l4 = self.sigma(np.dot(__l3, self.__w3))
			#error + change calc
			__l4_error = self.__y[__z:(__z+5)] - __l4    
			__l4_change = __l4_error*self.sigmaDeriv(__l4)
			__l3_error = __l4_change.dot(self.__w3.T)
			__l3_change = __l3_error * self.sigmaDeriv(__l3)
 			__l2_error = __l3_change.dot(self.__w2.T)
 			__l2_change = __l2_error * self.sigmaDeriv(__l2)
 			__l1_error= __l2_change.dot(self.__w1.T)
 			__l1_change = __l1_error * self.sigmaDeriv(__l1)
 			#update weights
   			self.__w3 += np.dot(__l3.T, __l4_change)
 			self.__w2 += np.dot(__l2.T, __l3_change)
   			self.__w1 += np.dot(__l1.T, __l2_change)
   			self.__w0 += np.dot(__l0.T, __l1_change)
   			__z += 5
   	def processCards(self,card01,card02):
   		if card01[:1] == 'T': __c1 = 10
   		elif card01[:1] == 'J': __c1 = 11
   		elif card01[:1] == 'Q': __c1 = 12
   		elif card01[:1] == 'K': __c1 = 13
   		elif card01[:1] == 'A': __c1 = 14
   		else: __c1 = int(card01[:1])
   		if card02[:1] == 'T': __c2 = 10
   		elif card02[:1] == 'J': __c2 = 11
   		elif card02[:1] == 'Q': __c2 = 12
   		elif card02[:1] == 'K': __c2 = 13
   		elif card02[:1] == 'A': __c2 = 14
   		else: __c2 = int(card02[:1])
   		if card01[-1:]==card02[-1:]: __s = 1
   		else: __s = 0
   		__c1 = float(__c1)/14
   		__c2 = float(__c2)/14
   		return [__c1,__c2,__s]

card1 = raw_input("Card 1: ")
card2 = raw_input("Card 2: ")
sdg_nn().setAction(card1,card2)
print str(sdg_nn().getAction())
