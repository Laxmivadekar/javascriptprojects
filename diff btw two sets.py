# Python Program to find the L.C.M. of two input number

'''def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(2 ,6))
# print(lcm(15, 17))'''

# GCD of more than two (or array) numbers
# This function implements the Euclidian
# algorithm to find H.C.F. of two number

# def find_gcd(x, y):
# 	while(y):
# 		x, y = y, x % y
# 	return x	
# l = [24,36]
# num1=l[0]
# num2=l[1]
# gcd=find_gcd(num1,num2)
# for i in range(2,len(l)):
# 	gcd=find_gcd(gcd,l[i])	def find_gcd(x, y):
# 	while(y):
# 		x, y = y, x % y
# 	return x	
# l = [24,36]
# num1=l[0]
# num2=l[1]
# gcd=find_gcd(num1,num2)
# for i in range(2,len(l)):
# 	gcd=find_gcd(gcd,l[i])
# print(gcd)
# Code contributed by Mohit Gupta_OMG

from math import gcd
a = [2,6]   #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)


def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
A = [12, 24, 27, 30, 36]
res = A[0]
for c in A[1::]:
    res = gcd(res , c)
print(res)
