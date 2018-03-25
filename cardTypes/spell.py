#!/usr/bin/python3

from cardTypes.card import * 

class Spell(Card):

	def __init__(self, colors, effect, rarity, speed = 0):
		super().__init__(colors, effect, rarity, speed)

