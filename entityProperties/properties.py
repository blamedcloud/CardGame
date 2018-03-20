#!/usr/bin/python3


class Permanent(object):
	
	def __init__(self, permanent = False):
		self.isPermanent = permanent
		
	def __set__(self, obj, val):
		self.isPermanent = val
		
	def __get__(self, obj, objtype):
		return self.isPermanent

class Targetable(object):
	
	def __init__(self, targetable = False):
		self.isTargetable = targetable
		
	def __set__(self, obj, val):
		self.isTargetable = val

	def __get__(self, obj, objtype):
		return self.isTargetable

def Exhaustible(object):

	def __init__(self, exhaustible = False):
		self.isExhaustible = exhaustible

	def __set__(self, obj, val):
		self.isExhaustible = val

	def __get__(self, obj, objtype):
		return self.isExhaustible

def Depletable(object):
	
	def __init__(self, depletable = False):
		self.isDepletable = depletable

	def __set__(self, obj, val):
		self.isDepletable = val

	def __get__(self, obj, objtype):
		return self.isDepletable

def Damageable(object):

	def __init__(self, damageable = False):
		self.isDamageable = damageable

	def __set__(self, obj, val):
		self.isDamageable = val

	def __get__(self, obj, objtype):
		return self.isDamageable

def Destructible(object):

	def __init__(self, destructible = False):
		self.isDestructible = destructible

	def __set__(self, obj, val):
		self.isDesctructible = val

	def __get__(self, obj, objtype):
		return self.isDestructible

def Exilable(object):
	
	def __init__(self, exilable = False):
		self.isExilable = exilable

	def __set__(self, obj, val):
		self.isExilable = val

	def __get__(self, obj, objtype):
		return self.isExilable

def Controllable(object):

	def __init__(self, controllable = False):
		self.isControllable = controllable

	def __set__(self, obj, val):
		self.isControllable = val

	def __get__(self, obj, objtype):
		return self.isControllable

def Attachable(object):

	def __init__(self, attachable = False):
		self.isAttachable = attachable

	def __set__(self, obj, val):
		self.isAttachable = val

	def __get__(self, obj, objtype):
		return self.isAttachable
