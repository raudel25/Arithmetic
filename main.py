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

a=time.time()
print(big.sqrt(big(2),2))
b=time.time()
print('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165')


# print(big(2).ship_by_base(-2))