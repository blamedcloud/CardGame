#!/usr/bin/python3

from entityProperties.properties import BoolProperty

class Entity(object):

	targetable = BoolProperty()
	depletable = BoolProperty()
	permanent = BoolProperty()
	damageable = BoolProperty()
	destructible = BoolProperty()
	exilable = BoolProperty()
	stealable = BoolProperty()
	attachable = BoolProperty()
	exhaustible = BoolProperty()

	def __init__(self):
		pass
