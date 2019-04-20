#!/usr/bin/python3

from entityProperties.entity import Entity

class PlayerEntity(Entity):

	def __init__(self, playerAPI):
		super().__init__()
		self.playerAPI = playerAPI

		self.targetable = True
		self.damageable = True
