class Person:
	def __init__(self, name, height):
		self.name = name
		self.age = height
	
	def __int__(self):
		return self.age
	
	def __str__(self):
		return self.name

per1 = Person('猪八戒', 175)
print(str(per1))
print(int(per1))


'''
----------------------------------
|类型转换	| 对应的方法 |
|________________________|
|     int	      |   __int__        |
|		float	    |   __float__    |
|		  str	      |   __str__        |
|	 bool	    |   __bool__     |
-----------------------------------
'''