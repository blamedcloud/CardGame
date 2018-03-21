
from card import Card

class Creature(Card):

	def __init__(self, colors, effect, rarity, atk, hp, creatureType, speed = 0):
		super().__init__(self, colors, effect, rarity)
		self.atk = atk
		self.hp = hp
		self.speed = speed
		self.creatureType = creatureType

		self.depletable = True
		self.permanent = True
		self.damageable = True
		self.destructible = True
		self.exhaustible = True
		
