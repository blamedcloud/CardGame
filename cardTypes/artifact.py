
from entityProperties.colors import Colors
from card import Card

class Artifact(Card):

	def __init__(self, effect, rarity, speed = 0):
		super().__init__(self,[Colors['colorless']], effect, rarity)
		self.speed = speed

		self.depletable = True
		self.permanent = True
		self.destructible = True
		self.exhaustible = True 


