# 2018-4-30
# What is the smallest value of n such that an algorithm whose running time is 100n^2 runs faster than an algorithm whose running time is 2^n on the same machine?

import math

def fun1(x):
	return 100*x**2

def fun2(x):
	return 2**x 

def equal(fun1, fun2):
	x = 1
	while fun1(x) > fun2(x):
		x += 1
	print('Somewhere between %d and %d' % (x-1, x))
	return ((x, fun1(x), fun2(x)), ((x-1, fun1(x-1), fun2(x-1))))


print(equal(fun1, fun2))
