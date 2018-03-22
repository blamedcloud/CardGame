#!/usr/bin/python3

from cardTypes.card import * 

class Creature(Card):

	def __init__(self, colors, effect, rarity, atk, hp, creatureType, speed = 0):
		super().__init__(colors, effect, rarity)
		self.base_atk = atk
		self.current_atk = self.base_atk
		self.base_hp = hp
		self.current_hp = self.base_hp
		self.speed = speed
		self.creatureType = creatureType

		self.depletable = True
		self.permanent = True
		self.damageable = True
		self.destructible = True
		self.exhaustible = True
		
