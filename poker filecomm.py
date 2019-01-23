#########
#IMPORTS#
#########
import itertools, random, sys, math, time
#from Tkinter import *
from random import randint
from time import sleep


######
#GAME#
######
def game():
	File().clear()
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
		File().clear()
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


#######
#SETUP#
#######
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

class ai:
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


#########
#BETTING#
#########
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
				human.money = human.money - rhuman.aiseAmount 
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
	#print "Ai, your cards are: " + str(ai.card1) + ", " + str(ai.card2)
	#ai.action = raw_input("What is your move? (r/c/f): ")
	print "AI's move."
	File().writeMoney()
	File().writeReady('m')
	ai.action = File().getMove()
	File().writeReady('f')
	if ai.action == 'f':
		print "AI folds."
		human.score = human.score + 1
		Table.winner = 'Human'
		Table.won = True
		return True
	elif ai.action == 'r':
		#ai.raiseAmount = input("Raise by: ")
		File().writeReady('r')
		ai.raiseAmount = File().getRaise()
		print "AI raises by " + str(File().getRaise())
		File().writeReady('f')
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
	File().writeCards(1)
	if bettingRound() == False:
		print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3)
		File().writeCards(2)
		if bettingRound() == False:
			print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3) + ", " + str(Table.turn)
			File().writeCards(3)
			if bettingRound() == False:
				print "The table's cards are: " + str(Table.flop1) + ", " + str(Table.flop2) + ", " + str(Table.flop3) + ", " + str(Table.turn) + ", " + str(Table.river)
				File().writeCards(4)
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


#################
#CARD EVALUATION#
#################
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

def card_ranks(hand):
    ranks = [14 if r == 'A' else
             13 if r == 'K' else
             12 if r == 'Q' else
             11 if r == 'J' else
             10 if r == 'T' else
             int(r)
             for r, s in hand]
    ranks.sort(reverse = True)
    return ranks if ranks != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]

def straight(ranks):
    return sum(ranks) - min(ranks)*5 == 10

def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))

def kind(n, ranks):
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
    return None


##########
#FILE I/O#
##########
class File:
	cardLine = ""
	moneyLine = ""
	wonLine = ""
	endLine = ""
	readyLine = ""

	def update(self):
		self.clear()
		f = open('aicom.txt', 'r+')
		f.write(str(self.cardLine))
		f.write("\n")
		f.write(str(self.moneyLine))
		f.write("\n")
		f.write(str(self.wonLine))
		f.write("\n")
		f.write(str(self.endLine))
		f.write("\n")
		f.write(str(self.readyLine))
		f.close()

	def clear(self):
		f = open('aicom.txt', 'r+')
		f.seek(0)
		f.truncate()
		f.close()

	def writeCards(self, x):
		if x == 1: self.cardLine = str(ai.card1)+' '+str(ai.card2)
		elif x == 2: self.cardLine = str(ai.card1)+' '+str(ai.card2)+' '+str(Table.flop1)+' '+str(Table.flop2)+' '+str(Table.flop3)
		elif x == 3: self.cardLine = str(ai.card1)+' '+str(ai.card2)+' '+str(Table.flop1)+' '+str(Table.flop2)+' '+str(Table.flop3)+' '+str(Table.turn)
		elif x == 4: self.cardLine = str(ai.card1)+' '+str(ai.card2)+' '+str(Table.flop1)+' '+str(Table.flop2)+' '+str(Table.flop3)+' '+str(Table.turn)+' '+str(Table.river)
		self.update()

	def writeReady(self,x):
		if x == 'm': self.readyLine = 'move'
		elif x == 'r': self.readyLine = 'raise'
		elif x == 'f': self.readyLine = 'not'
		self.update()

	def writeMoney(self):
		self.moneyLine = ai.money
		self.update()

	def writeWon(self, x):
		if x == 't': self.wonLine = 'won'
		elif x == 'f': self.wonLine = 'lost'
		self.update()

	def writeEnd(self, x):
		if x == 't': self.wonLine = 't'
		elif x == 'f': self.wonLine = 'f'
		self.update()


	# def isReady(self):
	# 		f = open('aimove.txt', 'r+')
	# 		f.seek(0)
	# 		fready = f.readlines()[3]
	# 		f.close()
	# 		if fready == 'ready': return True
	# 		else: return False

	def getMove(self):
		while True:
			# if self.isReady == True:
			# 	f = open('aimove.txt', 'r+')
			# 	f.seek(0)
			# 	fmove = f.readlines()[1]
			# 	f.close()
			# 	return str(fmove)
			# else:
			# 	print "waiting for AI"
			# 	time.sleep(1)
			f = open('aimove.txt', 'r+')
			f.seek(0)
			fmove = f.readlines()[0]
			f.close()
			if fmove == 'not':
				print 'waiting for AI'
			elif fmove == 'r' or fmove == 'c' or fmove == 'f':
				return str(fmove)
			

		
	def getRaise(self):
		while True:
			if self.isReady == False:
				print "waiting for AI"
				time.sleep(1)
			else:
				f = open('aimove.txt', 'r+')
				f.seek(0)
				fraise = f.readlines()[2]
				f.close()
				return int(fraise)
			

#############
#RUN PROGRAM#
#############
game()