

class Grammar(object):
	
	def __init__(self, grammarFile):
		full_text = ""
		with open(grammarFile) as FILE:
			for line in FILE:
				full_text += line
		full_text = full_text.replace("\n"," ")
		ruleList = full_text.split(';')




class Rule(object):
	
	def __init__(self, lhs, rhs):
		self.terminals = set()
		self.nonTerminals = {}
		
