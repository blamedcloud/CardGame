#!/usr/bin/python3



class Effect(object):

	def __init__(self, timingManager):
		self.abilities = []
		self.timingManager = timingManager

	def addAbility(self, ability, timing = None):
		self.abilities.append(ability)
		if timing != None:
			self.timingManager.register(timing, ability)

	def __len__(self):
		return len(self.abilities)

		
