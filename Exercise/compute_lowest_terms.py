## TODO: complete the function "lowest_terms" below
from math import gcd 


def lowest_terms(x):
	num, den = x.split('/')
	num = int(num)
	den = int(den)
	x = reduceFraction(num, den)
	return x 

	

def reduceFraction(num, den):
    d = gcd(num, den)
    num = num // d
    den = den // d
    x = str(num) + '/' + str(den)
    return x