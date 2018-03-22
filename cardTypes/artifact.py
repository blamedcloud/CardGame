#!/usr/bin/python3

from entityProperties.colors import Colors
from cardTypes.card import * 

class Artifact(Card):

	def __init__(self, effect, rarity, speed = 0):
		super().__init__([Colors['colorless']], effect, rarity)
		self.speed = speed

		self.depletable = True
		self.permanent = True
		self.destructible = True
		self.exhaustible = True 


