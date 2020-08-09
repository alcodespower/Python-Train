# 当对实例后面直接加括号时，python将自动调用__call__方法。
class Sname():
	def __init__(self, name, age):
		print('__init__被调用')
		self.name = name
		self.age = age
		
	def __call__(self, *args, **kwargs):
		print('__call__被调用了')
Sname1 = Sname('ALK', 20)
Sname1()