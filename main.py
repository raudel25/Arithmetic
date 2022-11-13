import math
from mpmath import mp
import time
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from decimal import Decimal
from big_num.numbers import BigNum
from big_num.numbers_decimal import BigNumDecimal
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
import other_arithmetics.fraction
from decimal import *
from other_arithmetics.extended754_num import Extended754Num
from big_num.basic_operations import karatsuba_algorithm, sub_number

big = BigNum()
bigg = BigNumDecimal()
frac = FractionNum()
dec = DecimalNum()
extend=Extended754Num(3,12,53)
getcontext().prec = 200
a = time.time()
print(extend(2)+extend(1))
b = time.time()
print(b - a)
