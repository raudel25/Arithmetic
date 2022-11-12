import math
from mpmath import mp
import time
from other_arithmetics.fraction import FractionNum
from big_num.numbers import  BigNum
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
import other_arithmetics.fraction
from decimal import *
from big_num.basic_operations import karatsuba_algorithm,sub_number

# print(extendended754_num.math.sin(b,base2))
# print(math.sin(2))
big = BigNum(precision=20)
frac=FractionNum()

#
# a = big('720')
# b = big('7')
# c=big('0')
#
# print(a*b)
# # for i in range(10):
# #     print(b)
# #     b+=a
x=time.time()
m=frac.pi()
print(m.numerator/m.denominator)
print(math.pi)
print(big.pi())
y=time.time()
print(y-x)
# x=big(48/17)-big(32/17)*big(0.458)
#
# for _ in range(10):
#     x=x+x*(big(1)-big(0.458)*x)

print(big('1')/big('3'))