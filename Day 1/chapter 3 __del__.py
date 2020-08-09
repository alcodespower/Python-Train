# 当删除对象时，python解释器会默认调用__del__方法
# 首先复习一下__init__
class Sname():
	def __init__(self, name, age):
		print('__init__被调用')
		self.name = name
		self.age =age
		
	def __del__(self):
		print('__del__被调用')
Sname2 = Sname('王明', 20)
del Sname2
print(1)

