import math
from mpmath import mp
import time
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from decimal import Decimal
from big_num.numbers import BigNum
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
import other_arithmetics.fraction
from decimal import *
from other_arithmetics.extended754_num import Extended754Num
from big_num.basic_operations import karatsuba_algorithm, sub_number

big = BigNum(precision=100, ind_base10=1)
frac = FractionNum()
dec = DecimalNum()
extend = Extended754Num(3, 12, 53)
getcontext().prec = 200
a = time.time()
print(extend(2) + extend(1))
print(big.pi())
print(big.pi())
b = time.time()
print(b - a)
print(big(1) / big(3))

# 0, 0, 0, 0, 0, 200, 363, 877
q = 77324867246100375000
w = 877363200000000000000000
print(w // q)
print(877363 // 77)
