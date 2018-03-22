#!/usr/bin/python3

from entityProperties.entity import Entity
from enum import Enum

class Card(Entity):
    
	def __init__(self, colors, effect, rarity):
		super().__init__()
		self.speed = 0
		self.effect = effect
		self.colors = colors
		self.rarity = rarity

		self.targetable = True
		self.exilable = True
		self.stealable = True


class Rarity(Enum):
	common = 4
	rare = 3
	epic = 2
	legendary = 1
