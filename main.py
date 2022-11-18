import time
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from big_num.numbers import BigNum
from other_arithmetics.extended754_num import Extended754Num

big = BigNum()
frac = FractionNum()
dec = DecimalNum()
extend = Extended754Num(2, 100, 53,repr_base=10)