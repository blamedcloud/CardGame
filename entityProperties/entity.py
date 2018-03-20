#!/usr/bin/python3

from properties import *

class Entity(object):
	targetable = Targetable()
	depletable = Depletable()
	permanent = Permanent()
	damageable = Damageable()
	destructible = Destructible()
	exilable = Exilable()
	controllable = Controllable()
	attachable = Attachable()
	exhaustible = Exhaustible()


e = Entity()

print(e.exilable)

print(e.targetable)	
