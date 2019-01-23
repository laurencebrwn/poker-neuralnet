###################################################
#-------------------DEPENDENCIES------------------#
###################################################
import itertools, random, sys, math, time, csv
from random import randint
from time import sleep
import numpy as np

def main():
	setup()
	train()
	DataSet().csvList()

def setup():
	CardPile().reset()
	CardPile().setList()

def train():
	for x in xrange(0,52):
		for y in xrange(0,52):
			if x!=y:
				tp = TrainPlayer((x,y))
				tp.setCards((CardPile().getSpecCard(tp.getCardNo()[0]),CardPile().getSpecCard(tp.getCardNo()[1])))
				for i in xrange(0,52):
					for j in xrange(0,52):
						if i!=j and i!=x and i!=y and j!=x and j!=y and x!=y:
							op = OppPlayer((i,j))
							op.setCards((CardPile().getSpecCard(op.getCardNo()[0]),CardPile().getSpecCard(op.getCardNo()[1])))
							for epoch in xrange(0,100):
								tbl = Table([CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard()])
								tp.setPoints(int(Compare().cardCompare(tp.getCards(),op.getCards(),tbl.getCards())))
								CardPile().reset()
								CardPile().usedCardAdd(tp.getCards()[0])
								CardPile().usedCardAdd(tp.getCards()[1])
								CardPile().usedCardAdd(op.getCards()[0])
								CardPile().usedCardAdd(op.getCards()[1])
							del op
				DataSet().setPoint(tp.getCards()[0],tp.getCards()[1],tp.getPoints())
				print tp.getCards()
				del tp
						
				
class Compare:
	__allTcards = []
	__all0cards = []
	def cardCompare(self,tpc,opc,tblc):
		self.__allTcards = [tpc[0], tpc[1], tblc[0], tblc[1], tblc[2], tblc[3], tblc[4]]
		self.__allOcards = [opc[0], opc[1], tblc[0], tblc[1], tblc[2], tblc[3], tblc[4]]
		if self.evaluateCard(self.__allTcards) > self.evaluateCard(self.__allOcards):
			return 1
		elif self.evaluateCard(self.__allOcards) > self.evaluateCard(self.__allTcards):
			return 0
		else:
			return 0

	def evaluateCard(self,hand):
	    groups = self.group(['--23456789TJQKA'.index(r) for r, s in hand])
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

	def group(self,items):
	    groups = [(items.count(x), x) for x in set(items)]
	    return sorted(groups, reverse = True)

class Table:
	__flop1 = []
	__flop2 = []
	__flop3 = []
	__turn = []
	__river = []
	def __init__(self,cards):
		self.__flop1 = cards[0]
		self.__flop2 = cards[1]
		self.__flop3 = cards[2]
		self.__turn = cards[3]
		self.__river = cards[4]
	def getCards(self):
		return [self.__flop1, self.__flop2, self.__flop3, self.__turn, self.__river]

class Player:
	__cardNo = []
	__cards = []
	def __init__(self, cardNo):
		self.__cardNo = cardNo
	def getCardNo(self):
		return self.__cardNo
	def setCards(self,cards):
		self.__cards = cards
	def getCards(self):
		return self.__cards

class TrainPlayer(Player):
	__points = 0
	def __init__(self, cardNo):
		Player.__init__(self, cardNo)
	def getCardNo(self):
		return Player.getCardNo(self)
	def setCards(self,cards):
		Player.setCards(self,cards)
	def getCards(self):
		return Player.getCards(self)
	def setPoints(self, points):
		self.__points += points
	def getPoints(self):
		return self.__points

class OppPlayer(Player):
	def __init__(self, cardNo):
		Player.__init__(self, cardNo)
	def getCardNo(self):
		return Player.getCardNo(self)
	def setCards(self,cards):
		Player.setCards(self, cards)
	def getCards(self):
		return Player.getCards(self)

class CardPile:
	__deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
	__usedCards  = []
	__list = []
	def getSpecCard(self,cardneeded):
		__specCard = self.__deck[cardneeded]
		self.__usedCards.append(__specCard)
		return __specCard
	def getRandCard(self):
		while True:
			__randCard = self.__deck[randint(0,51)]
			if __randCard not in self.__usedCards:
				self.__usedCards.append(__randCard)
				return __randCard
				break
	def setList(self):
		for x in xrange(0,52):
			for y in xrange(0,52):
				if y != x:
					self.__list.append((x,y))
	def getList(self):
		return self.__list
	def reset(self):
		del self.__usedCards[:]
	def usedCardAdd(self, card):
		self.__usedCards.append(card)
		
class DataSet:
	__cardList = []
	__pointList = []
	__floatList = []
	__predList = []
	def setPoint(self,card1,card2,point):
		self.__cardList.append(self.processCards(card1,card2))
		self.__pointList.append([point])
	def getPoint(self,pos):
		return (self.__cardList[pos], self.__pointList[pos])
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
   		c1 = float(c1)/14
   		c2 = float(c2)/14
   		return [c1,c2,s]
	def pointFloat(self):
		maxPoint = max(self.__pointList)[0]
		self.__floatList = [[float(j)/maxPoint for j in i] for i in self.__pointList]
	def makePred(self, x):
		return(
			1 if x >= 0.6 else
			0)
	def makePredList(self):
		self.__predList = [[self.makePred(x) for x in z] for z in self.__floatList] 
	def csvList(self):
		with open('handstrained.csv', 'wb') as myfile:
   			wr = csv.writer(myfile, delimiter=',')
   			for z in xrange(0,len(self.__cardList)):
   				wr.writerow(self.__cardList[z])
   		with open('correctpredtrainedUN.csv', 'wb') as myfile:
   			wr = csv.writer(myfile, delimiter=',')
   			for z in xrange(0,len(self.__pointList)):
   				wr.writerow(self.__pointList[z])
   		self.pointFloat()
   		self.makePredList()
   		with open('correctpredtrainedfloat.csv', 'wb') as myfile:
   			wr = csv.writer(myfile, delimiter=',')
   			for z in xrange(0,len(self.__floatList)):
   				wr.writerow(self.__floatList[z])
   		with open('correctpredtrained.csv', 'wb') as myfile:
   			wr = csv.writer(myfile, delimiter=',')
   			for z in xrange(0,len(self.__predList)):
   				wr.writerow(self.__predList[z])

main()