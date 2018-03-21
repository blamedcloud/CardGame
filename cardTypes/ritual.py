
from card import Card

class Ritual(Card):

	def __init__(self, colors, effect, rarity, speed = 0):
		super().__init__(self, colors, effect, rarity)
		self.speed = speed

		self.depletable = True
		self.permanent = True
		self.destructible = True
		self.exhaustible = True
