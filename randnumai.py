#########
#IMPORTS#
#########
import itertools, random, sys, math, time
#from Tkinter import *
from random import randint
from time import sleep


#########
#TEST AI#
#########
def ai():
	#File().writeMove('n')
	while Store.end != True:
		Store().update()
		time.sleep(2)
		if File().getReady() == 'move':
			File().writeMove(randMove())
			print "making move..."
			
		elif File().getReady() == 'raise':
			File().writeRaise(randint(1, Store.money/2))
			print "making raise...."
			
		elif Store.won == True: print "yey!"
		else: print "waiting..."

		while File().getReady() == 'not':
			time.sleep(2)
			File().writeMove('n')
		
		
def randMove():
	rand = randint(0,150)
	if  rand <= 50: 
		return 'f'
	elif rand <= 100 and rand > 50:
		return 'r'
	else: return 'c'



#############
#VALUE STORE#
#############
class Store:
	card1 = str
	card2 = str
	flop1 = str
	flop2 = str
	flop3 = str
	turn = str
	river = str
	money = int
	won = bool
	end = bool
	action = None
	raiseAmount = None
	
	def update(self):
		self.card1 = str(File().getCards()[:-(len(File().getCards())-len(File().getCards()[-2:]))])
		self.card2 = str((File().getCards()[3:])[:-(len(File().getCards()[3:])-len((File().getCards()[3:])[-2:]))])
		self.flop1 = str((File().getCards()[6:])[:-(len(File().getCards()[6:])-len((File().getCards()[6:])[-2:]))])
		self.flop2 = str((File().getCards()[9:])[:-(len(File().getCards()[9:])-len((File().getCards()[9:])[-2:]))])
		self.flop3 = str((File().getCards()[12:])[:-(len(File().getCards()[12:])-len((File().getCards()[12:])[-2:]))])
		self.turn = str((File().getCards()[15:])[:-(len(File().getCards()[15:])-len((File().getCards()[15:])[-2:]))])
		self.river = str((File().getCards()[18:])[:-(len(File().getCards()[18:])-len((File().getCards()[18:])[-2:]))])
		self.money = File().getMoney()
		self.won = File().getWon()
		self.end = File().getEnd()


##########
#FILE I/O#
##########
class File:
	moveLine = ""
	raiseLine = ""
	readyLine = ""
	def update(self):
		self.clear()
		f = open('aimove.txt', 'r+')
		f.write(self.moveLine)
		f.write("\n")
		f.write(self.raiseLine)
		# f.write("\n")
		# f.write(self.readyLine)
		f.close()

	def clear(self):
		f = open('aimove.txt', 'r+')
		f.seek(0)
		f.truncate()
		f.close()

	def writeMove(self, x):
		if x == 'f': 
			self.moveLine = 'f'
			print self.moveLine
		elif x == 'c': 
			self.moveLine = 'c'
			print self.moveLine
		elif x == 'r': 
			self.moveLine = 'r'
			print self.moveLine
		elif x == 'n':
			self.moveLine = 'not'
			print self.moveLine
		else: print 'reeee'
		self.update()

	def writeRaise(self,x):
		self.raiseLine = x
		self.update()

	# def writeReady(self, x):
	# 	if x == 't': self.readyLine = 'ready'
	# 	elif x == 'f': self.readyLine = 'not'
	# 	self.update()

	def getCards(self):
		f = open('aicom.txt', 'r+')
		fcards = f.readlines()[0]
		f.close()
		return str(fcards)

	def getReady(self):
		f = open('aicom.txt', 'r+')
		f.seek(0)
		fready = f.readlines()[4]
		f.close()
		print fready
		if fready == 'move' or fready == 'raise' or fready == 'not': return fready
		else: print "uhohhhh"

	def getMoney(self):
		f = open('aicom.txt', 'r+')
		f.seek(0)
		fmoney = f.readlines()[2]
		f.close()
		return str(fmoney)

	def getWon(self):
		f = open('aicom.txt', 'r+')
		f.seek(0)
		fwon = f.readlines()[3]
		f.close()
		if fwon == 'won':
			return True
		else:
			return False

	def getEnd(self):
		f = open('aicom.txt', 'r+')
		f.seek(0)
		fwon = f.readlines()[4]
		f.close()
		if fwon == 't':
			return True
		else:
			return False

ai()