import math
from mpmath import mp
import time
import big_num.math
import fraction_num.math
from big_num.numbers import Numbers, BigNum
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
import decimal_num.math
from decimal import *
from big_num.basic_operations import karatsuba_algorithm,sub_number

# print(extendended754_num.math.sin(b,base2))
print(math.sin(2))
big = BigNum(precision=1)

a = big('720')
b = big('7')
c=big('0')

print(a*b)
# for i in range(10):
#     print(b)
#     b+=a
x=time.time()
print(big_num.math.pi())
y=time.time()
print(y-x)
