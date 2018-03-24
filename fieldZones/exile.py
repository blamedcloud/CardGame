#!/usr/bin/python3

from fieldZones.zone import Zone

from entityProperties.properties import BoolProperty

class Exile(Zone):

	forever = BoolProperty()

	def __init__(self, forever = True):
		super().__init__()
		self.forever = forever

	def removeFrom(self, card):
		if self.forever:
			raise InvalidZoneTransition("One does not simply return from exile.", card, self)
		else:
			super().removeFrom(card)

	def sendTo(self, card, zone):
		if self.forever:
			raise InvalidZoneTransition("One does not simply return from exile.", card, self)
		else:
			super().sendTo(card, zone)
