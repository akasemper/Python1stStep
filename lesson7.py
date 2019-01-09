def pr (string, num):
	print (string, " ", num)
	pass

def summ (a, b):
	res = a + b
	return  res

def test (*args):
	print (args)
	pass

pr ("Number is", 56)
a = summ(23, 56)
pr("Numper is", a)

test("Hi", 23, 6.23)

mult = lambda x, y: x * y
print (mult(2, 5))
mult = lambda x, y: print(x * y)
(mult(20, 15))