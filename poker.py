#Import dependancies
import sys
from random import randint
import numpy as np

class Game:
	__gRound = 1
	__quit = False
	__reset = False
	__gName = ''
	__ai = None
	__human = None
	__gameOver = ''
	__table = None

	def __init__(self, gName):
		self.__gName = gName
		print "Welcome to texas holdem!"
	def setupGame(self):
	 	self.__human = Player(raw_input("Please enter your name: "))
	 	self.__ai = AI()
	 	self.__table = Table()
	 	self.__human.setMoney(953821)
	 	self.__ai.setMoney(1039868)
	def menu(self):
		while self.__quit == False:
			if self.__gRound == 1 or self.__reset == True:
				self.setupGame()
				self.__gRound = 1
			print "You are on round: " + str(self.__gRound)
			CardPile().reset()
			self.setupCards()
			print "Congratulations " + str(self.playGame()) + ", you won!"
			print "The AI's cards were: " + str(self.__ai.getCard())
			print str(self.__human.getName()) + ", your cards were: " + str(self.__human.getCard())
			print "The score is: AI: " + str(self.__ai.getScore()) + " | " + str(self.__human.getScore()) + " :" + str(self.__human.getName()).upper()
			if self.__gameOver == 'ai' or self.__gameOver == 'human':
				print "Since " + str(self.__gameOver) + " ran out of money the game is over. The game will now be reset."
				self.__reset = True
				if raw_input("Would you like to quit the game? (y/n):") == 'y': self.__quit = True
				else: self.__quit = False
			else:	
				self.__gRound = self.__gRound + 1
				if raw_input("Would you like to reset the game? (y/n):") == 'y': self.__reset = True
				else: self.__reset = False
				if raw_input("Would you like to quit the game? (y/n):") == 'y': self.__quit = True
				else: self.__quit = False
		sys.exit()
	def setupCards(self):
		self.__table.setCards()
		self.__human.setCard()
		self.__ai.setCard()
		self.__ai.reset()
	def playGame(self):
		self.__human.setMoney(-self.__table.getEntryMoney())
		self.__ai.setMoney(-self.__table.getEntryMoney())
		self.__table.setPot(2*self.__table.getEntryMoney())
		self.__table.setNextPlayer('r')
		if self.bettingRound() == False:
			print "The table's cards are: " + str(self.__table.getCards(0)+", "+self.__table.getCards(1)+", "+self.__table.getCards(2))
			self.__human.setAction('-')
			self.__ai.setAction('-')
			if self.bettingRound() == False:
				print "The table's cards are: " + str(self.__table.getCards(0)+", "+self.__table.getCards(1)+", "+self.__table.getCards(2)+", "+self.__table.getCards(3))
		        self.__human.setAction('-')
		    	self.__ai.setAction('-')
		    	if self.bettingRound() == False:
					print "The table's cards are: " + str(self.__table.getCards(0)+", "+self.__table.getCards(1)+", "+self.__table.getCards(2)+", "+self.__table.getCards(3)+", "+self.__table.getCards(4))
					self.__human.setAction('-')
					self.__ai.setAction('-')
					if self.bettingRound() == False:
						self.__table.setWinner(Compare().cardCompare(self.__human.getCard(), self.__ai.getCard(), [self.__table.getCards(0),self.__table.getCards(1),self.__table.getCards(2),self.__table.getCards(3),self.__table.getCards(4)]))
						if self.__table.getWinner() == 'Human':
							self.__human.setMoney(self.__table.getPot())
							self.__table.setPot(0)
							self.__human.setScore(1)
							self.__table.setWinnersCards(str(self.__human.getCard()))
							return str(self.__human.getName())
						elif self.__table.getWinner() == 'AI':
							self.__ai.setMoney(self.__table.getPot())
							self.__table.setPot(0)
							self.__ai.setScore(1)
							self.__table.setWinnersCards(str(self.__ai.getCard()))
							return 'AI'
						else:
							self.__human.setMoney(self.__table.getPot()/2)
							self.__ai.setMoney(self.__table.getPot()/2)
							self.__table.setPot(0)
							self.__table.setWinnersCards('')
							return 'no-one'
		else: 
			if self.__gameOver == 'ai':
				return str(self.__human.getName())
			if self.__gameOver == 'human':
				return 'AI'
			elif self.__table.getWinner() == 'Human':
				self.__table.setWinnersCards(str(self.__human.getCard()))
				return str(self.__human.getName())
			elif self.__table.getWinner() == 'AI':
				self.__table.setWinnersCards(str(self.__ai.getCard()))
				return 'AI'
			else:
				self.__table.setWinnersCards('')
				return 'no-one'
	def checkMoney(self,flag):
		if int(self.__human.getMoney()) < 0 and flag == False:
					self.__gameOver = 'human'
					self.__table.setWinner('AI')
					self.__table.setWon('t')
					self.__ai.setScore(1)
					return True
		elif int(self.__ai.getMoney()) < 0 and flag == False:
					self.__gameOver = 'ai'
					self.__table.setWinner('Human')
					self.__table.setWon('t')
					self.__human.setScore(1)
					return True
		elif flag == True: return True
		else: return False
	def bettingRound(self):
		self.__table.setWon('f')
		__flag = False
		if self.__table.getNextPlayer() == 1:
			while __flag == False: 
				__flag = self.checkMoney(__flag)
				print "Your money: " + str(self.__human.getMoney())
				print "AI money: " + str(self.__ai.getMoney())
				print "Pot: " + str(self.__table.getPot())
				if __flag == False:
					if self.bettingRoundHuman()== True and __flag == False:
						self.__table.setNextPlayer('a')
						__flag = True
				__flag = self.checkMoney(__flag)
				print "Your money: " + str(self.__human.getMoney())
				print "AI money: " + str(self.__ai.getMoney())
				print "Pot: " + str(self.__table.getPot())
				if __flag == False:
					if self.bettingRoundAi() == True and __flag == False:
						self.__table.setNextPlayer('h')
						__flag = True
		elif self.__table.getNextPlayer() == 2:
			while __flag == False:
				__flag = self.checkMoney(__flag)
				print "Your money: " + str(self.__human.getMoney())
				print "AI money: " + str(self.__ai.getMoney())
				print "Pot: " + str(self.__table.getPot())
				if __flag == False:
					if self.bettingRoundAi()== True and __flag == False:
						self.__table.setNextPlayer('h')
						__flag = True
				__flag = self.checkMoney(__flag)
				print "Your money: " + str(self.__human.getMoney())
				print "AI money: " + str(self.__ai.getMoney())
				print "Pot: " + str(self.__table.getPot())
				if __flag == False:
					if self.bettingRoundHuman() == True and __flag == False:
						self.__table.setNextPlayer('a')
						__flag = True
		if self.__table.getWon() == True: 
			return True
		else: 
			return False
	def bettingRoundAi(self):
		self.__ai.setAction('x')
		if self.__ai.getAction() == 'f':
			print "AI folds with the cards: " + str(self.__ai.getCard())
			self.__human.setMoney(self.__table.getPot())
			self.__table.setPot(0)
			self.__human.setScore(1)
			self.__table.setWinner('Human')
			self.__table.setWon('t')
			return True
		elif self.__ai.getAction() == 'r':
			self.__ai.setRaiseAmount()
			self.__ai.setMoney(-self.__ai.getRaiseAmount())
			self.__table.setPot(self.__ai.getRaiseAmount())
			print "AI raises by " + str(self.__ai.getRaiseAmount())
			if self.__human.getAction() == 'r':
				self.__ai.setMoney(-self.__human.getRaiseAmount())
				self.__table.setPot(self.__human.getRaiseAmount())
				self.__table.setWon('f')
				return False
			elif self.__human.getAction() == 'c':
				self.__table.setWon('f')
				return False
			else: 
				self.__table.setWon('f')
				return False
		elif self.__ai.getAction() == 'c':
			print "AI calls"
			if self.__human.getAction() ==  'r':
				self.__ai.setMoney(-self.__human.getRaiseAmount())
				self.__table.setPot(self.__human.getRaiseAmount())
				self.__table.setWon('f')
				return False
			elif self.__human.getAction() == 'c':
				self.__table.setWon('f')
				return True
			else: 
				self.__table.setWon('f')
				return False
	def bettingRoundHuman(self):
		print str(self.__human.getName())+", your cards are: " + str(self.__human.getCard())
		self.__human.setAction(raw_input("What is your move? (r/c/f): "))
		if self.__human.getAction() == 'f':
			self.__ai.setMoney(self.__table.getPot())
			self.__table.setPot(0)
			self.__ai.setScore(1)
			self.__table.setWinner('AI')
			self.__table.setWon('t')
			return True
		elif self.__human.getAction() == 'r':
			self.__human.setRaiseAmount(input("Raise by: "))
			self.__human.setMoney(-self.__human.getRaiseAmount())
			self.__table.setPot(self.__human.getRaiseAmount())
			if self.__ai.getAction() == 'r':
				self.__human.setMoney(-self.__ai.getRaiseAmount())
				self.__table.setPot(self.__ai.getRaiseAmount())
				self.__table.setWon('f')
				return False
			elif self.__ai.getAction() == 'c':
				self.__table.setWon('f')
				return False
			else:
				self.__table.setWon('f')
				return False
		elif self.__human.getAction() == 'c':
			if self.__ai.getAction() == 'c':
				self.__table.setWon('f')
				return True
			elif self.__ai.getAction() ==  'r':
				self.__human.setMoney(-self.__ai.getRaiseAmount())
				self.__table.setPot(self.__ai.getRaiseAmount())
				self.__table.setWon('f')
				return False
			else: 
				self.__table.setWon('f')
				return False
class Table:
	__flop1 = []
	__flop2 = []
	__flop3 = []
	__turn = []
	__river = []
	__entryMoney = 100
	__pot = 0
	__won = None
	__winner = ''
	__nextPlayer = None
	__winnersCards = ''

	def setCards(self):
		self.__flop1 = CardPile().getCard()
		self.__flop2 = CardPile().getCard()
		self.__flop3 = CardPile().getCard()
		self.__turn = CardPile().getCard()
		self.__river = CardPile().getCard()
	def getCards(self, amount):
		return [self.__flop1, self.__flop2, self.__flop3, self.__turn, self.__river][amount]
	def getEntryMoney(self):
		return self.__entryMoney
	def setPot(self, amount):
		if amount == 0:	self.__pot = amount
		else: self.__pot += amount
	def getPot(self):
		return self.__pot
	def setWinner(self,winner):
		self.__winner = str(winner)
	def getWinner(self):
		return self.__winner
	def setWon(self,tf):
		if tf == 't': self.__won = True
		elif tf == 'f': self.__won = False
	def getWon(self):
		return self.__won
	def setNextPlayer(self, x):
		if x == 'r':
			if randint(0,100) >= 50: 
				self.__nextPlayer = 1
			else:
				self.__nextPlayer = 2
		elif x == 'h':
			self.__nextPlayer = 1
		else:
			self.__nextPlayer = 2
	def getNextPlayer(self):
		return self.__nextPlayer
	def setWinnersCards(self,x):
		self.__winnersCards = str(x)
	def getWinnersCards(self):
		return self.__winnersCards

class Player:
	__card1 = []
	__card2 = []
	__money = 0
	__score = 0
	__action = ''
	__raiseAmount = 0
	__name = ''

	def __init__(self, name):
		self.__name = name
	def setCard(self):
		self.__card1 = CardPile().getCard()
		self.__card2 = CardPile().getCard()
	def getCard(self):
		return [self.__card1, self.__card2]
	def setMoney(self, amount):
		self.__money += amount
	def getMoney(self):
		return self.__money
	def setScore(self, amount):
		self.__score += amount
	def getScore(self):
		return self.__score
	def setAction(self, action):
		self.__action = action
	def getAction(self):
		return self.__action
	def setRaiseAmount(self, amount):
		self.__raiseAmount = amount
	def getRaiseAmount(self):
		return self.__raiseAmount
	def setName(self, name):
		self.__name = name
	def getName(self):
		return self.__name

class AI(Player):
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
	
	def __init__(self):
		Player.__init__(self, 'AI')
	def setCard(self):
		Player.setCard(self)
	def getCard(self):
		return Player.getCard(self)
	def setMoney(self, amount):
		Player.setMoney(self, amount)
	def getMoney(self):
		return Player.getMoney(self)
	def setScore(self, amount):
		Player.setScore(self, amount)
	def getScore(self):
		return Player.getScore(self)
	def setAction(self,x):
	    if x == '-':
	       Player.setAction(self, x)
	    else:
		    Player.setAction(self, self.predict(Player.getCard(self)[0],Player.getCard(self)[1]))
	def getAction(self):
		return Player.getAction(self)
	def setRaiseAmount(self):
			Player.setRaiseAmount(self, int(*(self.__move)*(Player.getMoney(self)/2))/100)
	def getRaiseAmount(self):
		return Player.getRaiseAmount(self)
	def reset(self):
		self.__allReadyRaise = False
	#make sigma
	def sigma(self,x):
		return 1/(1+np.exp(-x))
	#sigma gradient
	def sigmaDeriv(self,x):
		return x*(1-x)
	def predict(self,card1,card2):
		__carray = self.processCards(card1,card2)
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
   	def processCards(self,card1,card2):
   		if card1[:1] == 'T': __c1 = 10
   		elif card1[:1] == 'J': __c1 = 11
   		elif card1[:1] == 'Q': __c1 = 12
   		elif card1[:1] == 'K': __c1 = 13
   		elif card1[:1] == 'A': __c1 = 14
   		else: __c1 = int(card1[:1])
   		if card2[:1] == 'T': __c2 = 10
   		elif card2[:1] == 'J': __c2 = 11
   		elif card2[:1] == 'Q': __c2 = 12
   		elif card2[:1] == 'K': __c2 = 13
   		elif card2[:1] == 'A': __c2 = 14
   		else: __c2 = int(card2[:1])
   		if card1[-1:]==card2[-1:]: __s = 1
   		else: __s = 0
   		__c1 = float(__c1)/14
   		__c2 = float(__c2)/14
   		return [__c1,__c2,__s]

class Compare:
	__allHcards = []
	__allAcards = []
	def cardCompare(self,hc,ac,tblc):
		self.__allHcards = [hc[0], hc[1], tblc[0], tblc[1], tblc[2], tblc[3], tblc[4]]
		self.__allAcards = [ac[0], ac[1], tblc[0], tblc[1], tblc[2], tblc[3], tblc[4]]
		if self.evaluateCard(self.__allHcards) > self.evaluateCard(self.__allAcards): return 'Human'
		elif self.evaluateCard(self.__allAcards) > self.evaluateCard(self.__allHcards): return 'AI'
		else: return "no-one"

	def evaluateCard(self,hand):
	    __groups = self.group(['--23456789TJQKA'.index(r) for r, s in hand])
	    __counts, __ranks = zip(*__groups)
	    if __ranks == (14, 5, 4, 3, 2):
	        __ranks = (5, 4, 3, 2, 1)
	    __straight = len(__ranks) == 5 and max(__ranks)-min(__ranks) == 4
	    __flush = len(set([s for r, s in hand])) == 1
	    return (
	        9 if (5, ) == __counts else
	        8 if __straight and __flush else
	        7 if (4, 1) == __counts else
	        6 if (3, 2) == __counts else
	        5 if __flush else
	        4 if __straight else
	        3 if (3, 1, 1) == __counts else
	        2 if (2, 2, 1) == __counts else
	        1 if (2, 1, 1, 1) == __counts else
	        0), __ranks

	def group(self,items):
	    __groups = [(items.count(x), x) for x in set(items)]
	    return sorted(__groups, reverse = True)

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

game = Game('One')
game.menu()