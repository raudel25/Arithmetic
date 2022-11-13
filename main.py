import math
from mpmath import mp
import time
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from decimal import Decimal
from big_num.numbers import BigNum
from big_num.numbers_true_division import BigNumTrueDivision
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
import other_arithmetics.fraction
from decimal import *
from big_num.basic_operations import karatsuba_algorithm, sub_number

# print(extendended754_num.math.sin(b,base2))
# print(math.sin(2))
big = BigNum(precision=20, base10=10)
bigg = BigNumTrueDivision()
frac = FractionNum()
dec = DecimalNum()

#
# a = big('720')
# b = big('7')
# c=big('0')
#
# print(a*b)
# # for i in range(10):
# #     print(b)
# #     b+=a

# x=big(48/17)-big(32/17)*big(0.458)
#
# for _ in range(10):
#     x=x+x*(big(1)-big(0.458)*x)
getcontext().prec = 200
print(dec.sin(dec(10)))
a = time.time()
print(big.sin(big(10)))
b = time.time()
print(b - a)
print(bigg.pi())
print(bigg('6') / bigg('3'))
print()
