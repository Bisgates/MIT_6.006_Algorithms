# 2018-4-30
# Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in 8n^2 steps, while merge sort runs in 64n*lg(n) steps. For which values of n does insertion sort beat merge sort?

import math

def fun1(x):
	return 8*x**2

def fun2(x):
	return 64*x*math.log2(x)

def equal(fun1, fun2):
	x = 2
	while fun1(x) < fun2(x):
		x += 1
	print('\nWhen n is less than %d, insertion sert can be faster than merge sort; )\n' % (x))
	return ((x-1, fun1(x-1), fun2(x-1)), (x, fun1(x), fun2(x)))

print(equal(fun1, fun2))
