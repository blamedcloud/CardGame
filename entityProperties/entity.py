#!/usr/bin/python3

from properties import BoolProperty

class Entity(object):

	targetable = BoolProperty()
	depletable = BoolProperty()
	permanent = BoolProperty()
	damageable = BoolProperty()
	destructible = BoolProperty()
	exilable = BoolProperty()
	controllable = BoolProperty()
	attachable = BoolProperty()
	exhaustible = BoolProperty()


