
from entityProperties.properties import *

class Card(Targetable);
    
	def __init__(self, colors, effect):
		super().__init__(self, targetable = True)
		self.speed = 0
