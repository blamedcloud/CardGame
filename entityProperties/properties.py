


class Permanent(object):
	
	def __init__(self, permanent, *args, **kwargs):
		self.isPermanent = permanent
		
	def set_permanent(self, val):
		self.isPermanent = val
		

class Targetable(object):
	
	def __init__(self, targetable, *args, **kwargs):
		self.isTargetable = targetable
		
	def set_targetable(self, val):
		self.isTargetable = val
