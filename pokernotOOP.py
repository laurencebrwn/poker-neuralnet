###################################################
#-------------------DEPENDENCIES------------------#
###################################################
import itertools, random, sys, math, time
from random import randint
from time import sleep
import numpy as np

###################################################
#-----------------------GAME----------------------#
###################################################
def game():
	gRound = 0
	quit = False
	reset = False
	print "Welcome to texas holdem!"
	while quit == False:
		print "You are on round: " + str(gRound)
		if gRound == 0 or reset == True:
			setupGame()
			gRound = 0
		CardPile().reset()
		getCards()
		print "Congratulations " + playGame() + ", you won!"
		
		print "The score is: AI: " + str(ai.score) + " | " + str(human.score) + " :HUMAN"
		gRound = gRound + 1
		if raw_input("Would you like to reset the game? (y/n):") == 'y':
			reset = True
		else:
			reset = False
		if raw_input("Would you like to quit the game? (y/n):") == 'y':
			quit = True
		else:
			quit = False
	sys.exit()


###################################################
#----------------------SETUP----------------------#
###################################################
def setupGame():
	human.money = 50000
	ai.money = 50000
	Table.pot = 0
	human.score = 0
	ai.score = 0
	Table.startPlayer = bettingRoundOrder()
	Table.entrymoney = 100

class CardPile:
	__deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
	__usedCards  = []
	def getCard(self):
		while True:
			__randCard = self.__deck[randint(0,51)]
			if __randCard not in self.__usedCards:
				self.__usedCards.append(__randCard)
				return __randCard
				break
	def reset(self):
		self.__usedCards = []

class Table:
	flop1 = list
	flop2 = list
	flop3 = list
	turn = list
	river = list
	pot = int
	entrymoney = int
	won = None
	winner = None
	startPlayer= None
	

class human:
	card1 = list
	card2 = list
	money = int
	score = int
	action = None
	raiseAmount = None

def getCards():
		Table.flop1 = CardPile().getCard()
		Table.flop2 = CardPile().getCard()
		Table.flop3 = CardPile().getCard()
		Table.turn = CardPile().getCard()
		Table.river = CardPile().getCard()
		ai.card1 = CardPile().getCard()
		ai.card2 = CardPile().getCard()
		human.card1 = CardPile().getCard()
		human.card2 = CardPile().getCard()


###################################################
#--------------------BETTING----------------------#
###################################################
def bettingRoundHuman():
		print "Human, your cards are: " + str(human.card1) + ", " + str(human.card2)
		human.action = raw_input("What is your move? (r/c/f): ")
		if human.action == 'f':
			ai.score = ai.score + 1
			Table.winner = "Ai"
			Table.won = True
			return True
		elif human.action == 'r':
			human.raiseAmount = input("Raise by: ")
			if ai.action == 'r':
				human.money = human.money - ai.raiseAmount - human.raiseAmount
				Table.pot = Table.pot +  ai.raiseAmount + human.raiseAmount
				Table.won = False
				return False
			elif ai.action == 'c':
				human.money = human.money - human.raiseAmount 
				Table.pot = Table.pot + human.raiseAmount
				Table.won = False
				return False
			else:
				human.money = human.money - human.raiseAmount 
				Table.pot = Table.pot + human.raiseAmount
				Table.won = False
				return False
		elif human.action == 'c':
			if ai.action == 'c':
				Table.won = False
				return True
			elif ai.action ==  'r':
				human.money = human.money -  ai.raiseAmount
				Table.pot = Table.pot +  ai.raiseAmount
				Table.won = False
				return False
			else: 
				Table.won = False
				return False

def bettingRoundAi():
	ai.action = ai().amove()
	time.sleep(0.1)
	if ai.action == 'f':
		print "AI folds with the cards: " + ai.card1 + ', ' + ai.card2
		human.score = human.score + 1
		Table.winner = 'Human'
		Table.won = True
		return True
	elif ai.action == 'r':
		ai.raiseAmount = ai().araise()
		print "AI raises by " + ai.raiseAmount
		if human.action == 'r':
			ai.money = ai.money - human.raiseAmount - ai.raiseAmount
			Table.pot = Table.pot +  human.raiseAmount + ai.raiseAmount
			Table.won = False
			return False
		elif human.action == 'c':
			ai.money = ai.money - ai.raiseAmount 
			Table.pot = Table.pot + ai.raiseAmount
			Table.won = False
			return False
	elif ai.action == 'c':
		print "AI calls"
		if human.action ==  'r':
			ai.money = ai.money -  human.raiseAmount
			Table.pot = Table.pot +  human.raiseAmount
			Table.won = False
			return False
		elif human.action == 'c':
			Table.won = False
			return True
		else: 
			Table.won = False
			return False

def playGame():
	human.money = human.money - Table.entrymoney
	ai.money = ai.money - Table.entrymoney
	Table.pot = (Table.pot + 2*Table.entrymoney)
	
	if bettingRound() == False:
		print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3)
		
		if bettingRound() == False:
			print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3) + ", " + str(Table.turn)
			
			if bettingRound() == False:
				print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3) + ", " + str(Table.turn) + ", " + str(Table.river)
				
				if bettingRound() == False:
					return cardCompare()
	else: return Table.winner

def bettingRoundOrder():
	if randint(0,100) >= 50: 
		return 1
	else:
		return 2

def bettingRound():
	Table.won = False
	flag = False
	human.action = None
	ai.action = None
	human.raiseAmount = None
	ai.raiseAmount = None
	if Table.startPlayer == 1:
		while flag == False: 
			if flag == False:
				if bettingRoundHuman()== True:
					flag = True
				else: flag = False
			if flag == False:
				if bettingRoundAi() == True:
					flag = True
				else: flag = False
	elif Table.startPlayer == 2:
		while flag == False:
			if flag == False:
				if bettingRoundAi()== True:
					flag = True
				else: flag = False
			if flag == False:
				if bettingRoundHuman() == True:
					flag = True
				else: flag = False
	if Table.won == True: 
		return True
	else: 
		return False


###################################################
#-----------------CARD EVALUATION-----------------#
###################################################
def cardCompare():
	allHcards = [human.card1, human.card2, Table.flop1, Table.flop2, Table.flop3, Table.turn, Table.river]
	allAcards = [ai.card1, ai.card2, Table.flop1, Table.flop2, Table.flop3, Table.turn, Table.river]
	print evaluateCard(allHcards)
	print evaluateCard(allAcards)
	if evaluateCard(allHcards) > evaluateCard(allAcards):
		human.money = human.money + Table.pot
		Table.pot = 0
		human.score = human.score + 1
		return 'human'
	elif evaluateCard(allAcards) > evaluateCard(allHcards):
		ai.money = ai.money + Table.pot
		Table.pot = 0
		ai.score = ai.score + 1
		return 'ai'
	else:
		human.money = human.money + (Table.pot/2)
		ai.money = ai.money + (Table.pot/2)
		Table.pot = 0
		return "no-one"

def evaluateCard(hand):
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1
    return (
        9 if (5, ) == counts else
        8 if straight and flush else
        7 if (4, 1) == counts else
        6 if (3, 2) == counts else
        5 if flush else
        4 if straight else
        3 if (3, 1, 1) == counts else
        2 if (2, 2, 1) == counts else
        1 if (2, 1, 1, 1) == counts else
        0), ranks

def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)


###################################################
#-----------------------AI------------------------#
###################################################
class ai:
	card1 = list
	card2 = list
	money = int
	score = int
	action = ''
	raiseAmount = None

	def amove(self):
		#return str(self.randMove())
		return nn().predict(ai.card1,ai.card2)

	def araise(self):
		return randint(1, self.money/2)

	def randMove(self):
		rand = randint(0,150)
		if  rand <= 50: return 'f'
		elif rand <= 100 and rand > 50: return 'r'
		else: return 'c'

class nn:
	#define datasets
	x = np.genfromtxt('handstrained.csv', delimiter=',')
	y = np.genfromtxt('correctpredtrained.csv', delimiter=',')[np.newaxis]
	y = y.T
	
	#seed
	np.random.seed(1)

	#weights
	w0 = 2*np.random.random((3,4))-1
	w1 = 2*np.random.random((4,4))-1
	w2 = 2*np.random.random((4,4))-1
	w3 = 2*np.random.random((4,1))-1
	
	#make sigma
	def sigma(self,x):
		return 1/(1+np.exp(-x))

	#sigma gradient
	def sigmaDeriv(self,x):
		return x*(1-x)

	def predict(self,card1,card2):
		carray = self.processCards(card1,card2)
		for i in xrange(10):
			self.epoch()

   		#predict
		c1 = carray[0]
		c1 = int(c1)/14
		c2 = carray[1]
		c2 = int(c2)/14
		s = carray[2]
		avg = (c1+c2)/2
		C = np.array([[c1,c2,s,avg,abs(s-c1),abs(s-c2)]])
		move = self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(C, self.w0)), self.w1)), self.w2)), self.w3))
		if move >= 0.7: return 'r'
		elif move >=0.5: return 'c'
		else: return 'f'

	def epoch(self):
		z=0
		
		#train
		for t in xrange(len(y)/4):
			#forward propagation
			l0 = self.x[z:(z+5)]
  			l1 = self.sigma(np.dot(l0, self.w0))
   			l2 = self.sigma(np.dot(l1, self.w1))
  			l3 = self.sigma(np.dot(l2, self.w2))
  			l4 = self.sigma(np.dot(l3, self.w3))
   
			#error + change calc
			l4_error = self.y[z:(z+5)] - l4    
			l4_change = l4_error*self.sigmaDeriv(l4)
			l3_error = l4_change.dot(self.w3.T)
			l3_change = l3_error * self.sigmaDeriv(l3)
 			l2_error = l3_change.dot(self.w2.T)
 			l2_change = l2_error * self.sigmaDeriv(l2)
 			l1_error= l2_change.dot(self.w1.T)
 			l1_change = l1_error * self.sigmaDeriv(l1)
  	
 			#update weights
   			self.w3 += np.dot(l3.T, l4_change)
 			self.w2 += np.dot(l2.T, l3_change)
   			self.w1 += np.dot(l1.T, l2_change)
   			self.w0 += np.dot(l0.T, l1_change)
   			z += 5

   	def processCards(self,card1,card2):
   		if card1[:1] == 'T': c1 = 10
   		elif card1[:1] == 'J': c1 = 11
   		elif card1[:1] == 'Q': c1 = 12
   		elif card1[:1] == 'K': c1 = 13
   		elif card1[:1] == 'A': c1 = 14
   		else: c1 = int(card1[:1])
   		if card2[:1] == 'T': c2 = 10
   		elif card2[:1] == 'J': c2 = 11
   		elif card2[:1] == 'Q': c2 = 12
   		elif card2[:1] == 'K': c2 = 13
   		elif card2[:1] == 'A': c2 = 14
   		else: c2 = int(card2[:1])
   		if card1[-1:]==card2[-1:]: s = 1
   		else: s = 0
   		return [c1,c2,s]

###################################################
#-------------------RUN PROGRAM-------------------#
###################################################
game()