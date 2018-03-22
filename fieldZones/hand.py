#!/usr/bin/python3

from fieldZones.zone import Zone

class Hand(Zone):

	def __init__(self, maxSize = 10):
		super().__init__()
		self.maxSize = 10

		self.ordered = True

	def reduceToMaxSize(self, graveyard):
		while len(self) > self.maxSize:
			self.sendTo(self.cardsInZone[0],graveyard)
