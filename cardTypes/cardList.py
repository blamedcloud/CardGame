#!/usr/bin/python3

from cardTypes.card import Card

class CardList(object):

	def __init__(self, startingCards = None):
		self.cards = []
		if isinstance(startingCards, CardList):
			self.cards = startingCards.cards
		else:
			self.extend(startingCards)



# below are the standard methods to emulate a list type
	def __len__(self):
		return len(self.cards)

	def __getitem__(self, key):
		return self.cards[key]

	def __setitem__(self, key, value):
		if not isinstance(value, Card):
			raise TypeError
		else:
			self.cards[key] = value

	def __delitem__(self, key):
		self.cards.__delitem__(key)

	def __iter__(self):
		return self.cards.__iter__()

	def __reversed__(self):
		return self.cards.__reversed__()

	def __contains__(self, item):
		if not isinstance(item, Card):
			return False
		else:
			return self.cards.__contains__(item)

	def append(self, item):
		if not isinstance(item, Card):
			raise TypeError
		else:
			self.cards.append(item)

	def count(self, item):
		return self.cards.count(item)

	def index(self, item, start = None, end = None):
		if start == None:
			return self.cards.index(item)
		else:
			if end == None:
				return self.cards.index(item, start)
			else:
				return self.cards.index(item, start, end)

	def extend(self, iterable):
		for item in iterable:
			if not isinstance(item, Card):
				raise TypeError
			else:
				self.cards.append(item)

	def insert(self, i, item):
		if not isinstance(item, Card):
			raise TypeError
		else:
			self.cards.insert(i,item)

	def pop(self, index = None):
		if index == None:
			return self.cards.pop()
		else:
			return self.cards.pop(index)

	def remove(self, item):
		self.cards.remove(item)

	def reverse(self):
		self.cards.reverse()

	def sort(self, _key = None, _reverse = False):
		self.cards.sort(key=_key, reverse = _reverse)

	def __add__(self, other):
		if not isinstance(other, CardList):
			return NotImplemented
		else:
			return CardList(self.cards + other.cards)

	def __radd__(self, other):
		if not isintance(other, CardList):
			return NotImplemented
		else:
			return CardList(other.cards + self.cards)

	def __iadd__(self, other):
		if not isinstance(other, CardList):
			return NotImplemented
		else:
			self.cards += other.cards
			return self


