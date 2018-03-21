
from entityProperties.entity import Entity

class Card(Entity);
    
	def __init__(self, colors, effect, rarity):
		super().__init__(self)
		self.speed = 0
		self.effect = effect
		self.colors = colors
		self.rarity = rarity

		self.targetable = True
		self.exilable = True
		self.controllable = True


class Rarity(Enum):
	common = 4
	rare = 3
	epic = 2
	legendary = 1
