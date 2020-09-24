## TODO: complete the function "lowest_terms" below
from math import gcd 


def lowest_terms(x):
	num, den = x.split('/')
	num = int(num)
	den = int(den)
	if num and den > 0:
		x = reduceFraction(num, den)
		return x 
	elif num > 0 and den < 0:
		x = reduceFraction(num, den)
		num, den = x.split('/')
		num = int(num)
		den = int(den)
		num = num * -1
		den = den * -1
		x = str(num) + '/' + str(den)
		return x 
	elif num < 0 and den > 0:
		x = reduceFraction(num, den)
		return x
	elif num < 0 and den < 0:
		x = reduceFraction(num, den)
		num, den = x.split('/')
		num = int(num)
		den = int(den)
		num = num * -1
		den = den * -1
		x = str(num) + '/' + str(den)
		return x 
	elif den == 0:
		x = "Undefined"
		return x 
	elif num == 0:
		x = "0"
		return x

	

def reduceFraction(num, den):
    d = gcd(num, den)
    num = num // d
    den = den // d
    x = str(num) + '/' + str(den)
    return x