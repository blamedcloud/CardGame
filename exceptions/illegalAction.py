#!/usr/bin/python3

class IllegalAction(Exception):
	
	def __init__(self, message, card):
		self.card = card
		self.message = message


class InvalidTarget(IllegalAction):

	def __init__(self, message, card):
		super().__init__(card, message)

class InvalidZoneTransition(IllegalAction):

	def __init__(self, message, card, zone):
		super().__init__(card, message)
		self.zone = zone


