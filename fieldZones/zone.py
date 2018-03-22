#!/usr/bin/python3

from entityProperties.entity import Entity
from entityProperties.properties import BoolProperty

from cardType.cardList import CardList


class Zone(Entity):

	ordered = BoolProperty()
	hidden = BoolProperty()

	def __init__(self):
		super().__init__()
		self.cardsInZone = CardList()

		self.targetable = True

	def addTo(self, card):
		self.cardsInZone.append(card)

	def removeFrom(self, card):
		self.cardsInZone.remove(card)

	def sendTo(self, card, zone):
		self.cardsInZone.remove(card)
		zone.addTo(card)

	def __contains__(self, card):
		return card in self.cardsInZone

	def __len__(self):
		return len(self.cardsInZone)

	def __str__(self):
		if self.hidden:
			return "Size: " + str(len(self)):
		else:
			val = ""
			if self.ordered:
				val = "<BOTTOM>\n"
				for index, card in enumerate(self.cardsInZone):
					val += str(index) + ". " + str(card) + "\n"
				val += "<TOP>\n"
			else:
				for card in self.cardsInZone:
					val += str(card) + "\n"
			return val
