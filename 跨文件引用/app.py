from const import PI


def calc_round_area(radius):
	return PI * (radius ** 2)


def main():
	print("round area: ", calc_round_area(2))


main()

'''
运行结果：
PI: 3.14
round area:  12.56
'''