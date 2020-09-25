## TODO: complete the function "lowest_terms" below 

def lowest_terms(x):
	"""Returns the lowest term of the string x
	
	x(str) - The number whose lowest term is to be found 
	"""
	num, den = x.split('/')
	num = int(num)
	den = int(den)
	if den == 0:
		x = "Undefined"
		return x 
	elif num == 0:
		x = "0"
		return x
	else:
		x = reduceFraction(num, den)
		return x 


def common_divisor(x, y):
	"""This function collects 2 numbers and returns the common divisor
	
	x(int)- The first number 
	y(int)- the second number 
	"""
	while (y):
		x, y = y, x % y
	return x 

def reduceFraction(num, den):
	"""This function collects a fraction numerator and denominator and reduces the fraction to the lowest term and returns 
		a string of the reduced fraction
	num(int)- The numerator of the fraction
	den(int)- The denominator of the fraction
	""" 
	a = common_divisor(num, den)
	num = num // a  
	den = den // a 
	x = str(num) + '/' + str(den)
	return x