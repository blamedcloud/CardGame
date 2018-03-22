#!/usr/bin/python3

from cardTypes.card import *
from cardTypes.creature import Creature
from cardTypes.cardList import CardList

from entityProperties.colors import Colors


cl = CardList()

card1 = Card([Colors.blue], None, Rarity.common)

card2 = Creature([Colors.blue], None, Rarity.common, 1, 1, "Bird", 1)

cl.append(card1)

cl.append(card2)

print(cl)

for item in cl:
	print(item)
