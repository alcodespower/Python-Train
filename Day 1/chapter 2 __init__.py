# __init__方法
class  Sname():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
Sname1 = Sname('ALK',21)
print(Sname1)

'''
一般情况下，直接对实例使用print()语句，
输出结果是<__main__.类名 object at 内存地址>
此处打印出：
<__main__.Sname object at 0x7f38ba739c10>
'''

class Sname_plus():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		print(Sname_plus)
		return 'Sname_plus [name = %s, age = %d]'  % (self.name,self.age)
	
Sname2 = Sname_plus('ALK_plus',21)
print(Sname2)

'''
这里的str()会将对象转化为字符串 将指定的对象转化为字符串的结果
Sname_plus [name = ALK_plus, age = 21]
'''


'''
__repr__方法和__str__方法功能类似，
都是用来修改一个对象的默认打印内容。
在打印一个对象时，如果没有重写__str__方法，
它会自动来查找__repr__方法。
如果这两个方法都没有，会直接打印这个对象的内存地址。
'''

'''
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Hi'


class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'Hi'

    def __str__(self):
        return 'Hello'


a = Person('邢捕头', 34)
print(a) # Hi

b = Student('白展堂', 98)
print(b) # Hello
'''

'''
注意：
一般来说，
__str__方法的结果更加在意可读性，
而
__repr__方法的结果更加在意正确性。
'''