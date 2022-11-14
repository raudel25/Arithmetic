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
extend = Extended754Num(3, 12, 53)
getcontext().prec = 200

a=time.time()
print(big.sin(big(2)))
b=time.time()
print(b-a)
print(math.log(2))
print(big(0.4)*big(3)==big(1.2))
print(dec(0.4)*dec(3)==dec(1.2))
print('1,41421356237309504880168872420969807856967187537694 8073176679 3799')