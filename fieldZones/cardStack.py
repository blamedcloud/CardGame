#!/usr/bin/python3

from fieldZones.zone import Zone

class CardStack(Zone):

	def __init__(self):
		super().__init__()

		self.ordered = True
		self.minSpeed = 0

	def updateSpeed(self):
		if len(self) > 0:
			self.minSpeed = self.cardsInZone[-1].speed
		else:
			self.minSpeed = 0
		if self.minSpeed == -1:
			self.resolve() # might want to restructure this depending on how timing ends up working.

	def removeFrom(self, card):
		super().removeFrom(card)
		self.updateSpeed()

	def checkValidAddition(self, card):
		value = False
		cardSpeed = card.speed
		if cardSpeed == -2: # skip-stack speed. never goes on stack.
			value = False
		elif cardSpeed == -1: # stack auto-resolve speed. Always valid.
			value = True
		elif cardSpeed >= self.minSpeed:
			value = True
		return value

	def addTo(self, card):
		if not self.checkValidAddition(card):
			raise Exception("Card can't go on stack at this speed!")
		else:
			super().addTo(card)
			self.updateSpeed()

	def resolve(self):
		while len(self) > 0:
			topCard = self.cardsInZone.pop()

			# TODO: resolve the card...
			# will depend on how Effect() gets coded.
 
