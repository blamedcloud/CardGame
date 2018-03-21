#!/usr/bin/python3


class BoolProperty(object):

	def __init__(self, default=False):
		self.default = default
		self.values = {}

	def __get__(self, obj, objtype):
		return self.values.get(obj,self.default)

	def __set__(self, obj, val):
		self.values[obj] = bool(val)
