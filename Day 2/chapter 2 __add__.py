class stature():
	def __init__(self, ObjA, ObjB):
		self.ObjA = ObjA
		self.ObjB = ObjB
		
	def __add__(self, other):
		return self.ObjB + other
	
	def __sub__(self, other):
		return self.ObjB - other
	
	def __mul__(self, other):
		return self.ObjB * other
	
	def __truediv__(self, other):
		return self.ObjB / other
	
	def __mod__(self, other):
		return self.ObjB % other
	
	def __pow__(self, other):
		return self.ObjB ** other
	
dataA = stature(12,152)
print(dataA + 2)
print(dataA - 2)
print(dataA * 2)
print(dataA / 2)
print(dataA % 2)
print(dataA ** 2)