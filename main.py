import time
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from big_num.numbers import BigNum
from other_arithmetics.extended754_num import Extended754Num
from arithmetic_math.arithmetic_math import ArithmeticMath


def calculate_pi(arithmetic: 'ArithmeticMath'):
    time1 = time.time()
    arithmetic.pi()
    time2 = time.time()

    return time2 - time1


def calculate_e(arithmetic: 'ArithmeticMath'):
    time1 = time.time()
    arithmetic.e()
    time2 = time.time()

    return time2 - time1


big = BigNum(precision=10)
frac = FractionNum()
dec = DecimalNum()
extend = Extended754Num(2, 100, 53, repr_base=10)

print(calculate_pi(big))
print(calculate_pi(frac))
print(calculate_pi(dec))

print(calculate_e(big))
print(calculate_e(frac))
print(calculate_e(dec))

print(big(0.4)*big(3)==big(1.2))
print(frac(0.4)*frac(3)==frac(1.2))
print(dec(0.4)*dec(3)==dec(1.2))