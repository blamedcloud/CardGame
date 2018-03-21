
from card import Card

class Spell(Card):

	def __init__(self, colors, effect, rarity, speed = 0):
		super().__init__(self, colors, effect, rarity)
		self.speed = speed

