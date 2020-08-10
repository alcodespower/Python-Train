class compare():
	def __init__(self,ObjA, ObjB):
		self.ObjA = ObjA
		self.ObjB = ObjB
		
	def __eq__(self, other):
		print('__eq__被执行！')
		return self.ObjA == other.ObjA and self.ObjB == other.ObjB
	
	def __ne__(self, other):
		print('__ne__被执行！')
		return  self.ObjA == other.ObjA and self.ObjB == other.ObjB
	
	def __gt__(self, other):
		print('__gt__被执行！')
		return  self.ObjA > other.ObjA and self.ObjB > other.ObjB
	
	def __lt__(self, other):
		print('__lt__被执行！')
		return  self.ObjA < other.ObjA and self.ObjB < other.ObjB
	
	def __ge__(self, other):
		print('__lt__被执行！')
		return self.ObjA >= other.ObjA and self.ObjB >= other.ObjB
	
	def __le__(self, other):
		print('__le__被执行！')
		return self.ObjA <= other.ObjA and self.ObjB <= other.ObjB


ContainerA = compare(21,15)
ContainerB = compare(21,15)
ContainerC = compare(30,18)
print(ContainerA == ContainerB)# __eq__被执行！True
print(ContainerA == ContainerC)# __eq__被执行！False
print(ContainerA != ContainerC)# __ne__被执行！False
print(ContainerA > ContainerC)# __gt__被执行！False
print(ContainerA < ContainerC)# __lt__被执行！False
print(ContainerA >= ContainerC)# __lt__被执行！False
print(ContainerA <= ContainerC)# __lt__被执行！False


'''
比较运算符	调用的方法
per1 == per2  |	__eq__
per1 != per2   |	__ne__
per1 > per2    |  __gt__
per1 < per2    |	__lt__
per1 >= per2  |	__ge__
per1 <= per2	|  __le__
'''