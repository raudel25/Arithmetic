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

big = BigNum()
frac = FractionNum()
dec = DecimalNum()
extend = Extended754Num(2, 100, 53,repr_base=10)
# a=extend(1)
# b=extend(10,input_base=10)
# print(b)
print(extend.pi(precision=10))
print(big.pi())

# print(big(2).ship_by_base(-2))