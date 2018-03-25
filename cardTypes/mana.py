#!/usr/bin/python3

from cardTypes.card import *

class Mana(Card):

	def __init__(self, colors, effect, rarity):
		super().__init__(colors, effect, rarity, speed = -2)
		
		# self.speed = -2 # mana speed, doesn't go on stack.

		self.depletable = True
		self.exilable = False
		self.stealable = False
		self.exhaustible = True
