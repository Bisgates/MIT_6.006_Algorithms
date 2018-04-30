# 2018-4-30

import time as time
import math
from prettytable import PrettyTable

time_list = [1, 60, 60*60, 60*60*24, 60*60*24*30, 60*60*24*30*12, 60*60*24*30*12*100] 
time_list_name = ['second', 'minut', 'hour', 'day', 'month', 'year', 'centry']

def lgTime(n):
	t0 = time.time()
	for i in range(int(math.log2(n))):
		i = i
	per_s = n/(time.time()-t0)
	O_lg = [len(str(int(ele*per_s))) for ele in time_list]
	return O_lg	

def sqrtTime(n):
	t0 = time.time()
	for i in range(int(math.sqrt(n))):
		i = i
	per_s = n/(time.time()-t0)
	O_sqrt = [len(str(int(ele*per_s))) for ele in time_list]
	return O_sqrt

def linearTime(n):
	t0 = time.time()
	for i in range(n):
		i = i
	per_s = n/(time.time()-t0)
	O_linear = [int(ele*per_s) for ele in time_list]
	return O_linear
	
def nlgTime(n):
	t0 = time.time()
	for i in range(int(n*math.log2(n))):
		i = i
	per_s = n/(time.time()-t0)
	O_nlg = [int(ele*per_s) for ele in time_list]
	return O_nlg

def squareTime(n):
	t0 = time.time()
	for i in range(n**2):
		i = i
	per_s = n/(time.time()-t0)
	O_square = [int(ele*per_s) for ele in time_list]
	return O_square	

def cubicalTime(n):
	t0 = time.time()
	for i in range(n**3):
		i = i
	per_s = n/(time.time()-t0)
	O_cubical = [int(ele*per_s) for ele in time_list]
	return O_cubical

def ExponentialTime(n):
	t0 = time.time()
	for i in range(2**n):
		i = i
	per_s = n/(time.time()-t0)
	O_exponential = [int(ele*per_s) for ele in time_list]
	return O_exponential
	
def factorialTime(n):
	t0 = time.time()
	for i in range(math.factorial(n)):
		i = i
	per_s = n/(time.time()-t0)
	O_factorial = [int(ele*per_s) for ele in time_list]
	return O_factorial

print(lgTime(10**200))
print(sqrtTime(10**16))
print(linearTime(10**4))
print(nlgTime(10**3))
print(squareTime(10**3))
print(cubicalTime(10**2))
print(ExponentialTime(30))
# print(factorialTime(20))
