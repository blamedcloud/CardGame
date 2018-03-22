#!/usr/bin/python3

import random

from fieldZones.zone import Zone

class Deck(Zone):

	def __init__(self):
		super().__init__()

		self.ordered = True
		self.hidden = True

	def shuffle(self):
		self.cardsInZone.sort(key = lambda x: random.random())

	def draw(self, hand, num = 1):
		for x in range(num):
			card = self.cardsInZone.pop()
			hand.addTo(card)

	def putOnTop(self, card):
		self.cardsInZone.append(card)

	def putOnBottom(self, card):
		self.insert(0,card)


