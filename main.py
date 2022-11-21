import math
import time
from tabulate import tabulate
from other_arithmetics.fraction import FractionNum
from other_arithmetics.decimal import DecimalNum
from big_num.numbers import BigNum
import fractions
from decimal import *
from other_arithmetics.extended754_num import Extended754Num


def calculate_one_param(function):
    time1 = time.time()
    value = function()
    time2 = time.time()

    if type(value) == fractions.Fraction:
        value = value.numerator / value.denominator

    return [value, '&', time2 - time1, '\\\ \hline']


def calculate_two_param(function, number):
    time1 = time.time()
    value = function(number)
    time2 = time.time()

    if type(value) == fractions.Fraction:
        value = value.numerator / value.denominator

    return [value, '&', time2 - time1, '\\\ \hline']


def calculate_three_param(function, number1, number2):
    time1 = time.time()
    value = function(number1, number2)
    time2 = time.time()

    if type(value) == fractions.Fraction:
        value = value.numerator / value.denominator

    return [value, '&', time2 - time1, '\\\ \hline']


def calculate_pi(big_n, frac_n, dec_n):
    f = open('data/pi.txt', 'w')

    l = [['BigNum', '&'] + calculate_one_param(big_n.pi), ['FractionNum', '&'] + calculate_one_param(frac_n.pi),
         ['DecimalNum', '&'] + calculate_one_param(dec_n.pi)]

    f.write(tabulate(l))
    f.close()


def calculate_e(big_n, frac_n, dec_n):
    f = open('data/e.txt', 'w')

    l = [['BigNum', '&'] + calculate_one_param(big_n.e), ['FractionNum', '&'] + calculate_one_param(frac_n.e),
         ['DecimalNum', '&'] + calculate_one_param(dec_n.e)]

    f.write(tabulate(l))
    f.close()


def calculate_sin(big_n, frac_n, dec_n, number):
    f = open(f'data/sin{number}.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_n.sin, big_n(number)),
         ['FractionNum', '&'] + calculate_two_param(frac_n.sin, frac_n(number)),
         ['DecimalNum', '&'] + calculate_two_param(dec_n.sin, dec_n(number))]

    f.write(tabulate(l))
    f.close()


def calculate_cos(big_n, frac_n, dec_n, number):
    f = open(f'data/cos{number}.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_n.cos, big_n(number)),
         ['FractionNum', '&'] + calculate_two_param(frac_n.cos, frac_n(number)),
         ['DecimalNum', '&'] + calculate_two_param(dec_n.cos, dec_n(number))]

    f.write(tabulate(l))
    f.close()


def calculate_ln(big_n, frac_n, dec_n, number):
    f = open(f'data/ln{number}.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_n.ln, big_n(number)),['FractionNum', '&']+ calculate_two_param(frac_n.ln, frac_n(number)),
         ['DecimalNum', '&'] + calculate_two_param(dec_n.ln, dec_n(number))]

    f.write(tabulate(l))
    f.close()


def calculate_sqrt(big_n, frac_n, dec_n, number1, number2):
    f = open(f'data/sqrt{number1}_{number2}.txt', 'w')

    l = [['BigNum', '&'] + calculate_three_param(big_n.sqrt, big_n(number1), number2),
         ['FractionNum', '&'] + calculate_three_param(frac_n.sqrt, frac_n(number1), number2),
         ['DecimalNum', '&'] + calculate_three_param(dec_n.sqrt, dec_n(number1), number2)]

    f.write(tabulate(l))
    f.close()


def calculate_pow(big_n, frac_n, dec_n, number1, number2):
    f = open(f'data/pow{number1}_{number2}.txt', 'w')

    l = [['BigNum', '&'] + calculate_three_param(big_n.pow_value, big_n(number1), big_n(number2)),
         ['FractionNum', '&'] + calculate_three_param(frac_n.pow_value, frac_n(number1), frac_n(number2)),
         ['DecimalNum', '&'] + calculate_three_param(dec_n.pow_value, dec_n(number1), dec_n(number2))]

    f.write(tabulate(l))
    f.close()

def calculate_asin(big_n, frac_n, dec_n, number1):
    f = open(f'data/asin{number1}.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_n.asin, big_n(number1)),
         ['FractionNum', '&'] + calculate_two_param(frac_n.asin, frac_n(number1)),
         ['DecimalNum', '&'] + calculate_two_param(dec_n.asin, dec_n(number1))]

    f.write(tabulate(l))
    f.close()

def calculate_atan(big_n, frac_n, dec_n, number1):
    f = open(f'data/atan{number1}.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_n.atan, big_n(number1)),
         ['FractionNum', '&'] + calculate_two_param(frac_n.atan, frac_n(number1)),
         ['DecimalNum', '&'] + calculate_two_param(dec_n.atan, dec_n(number1))]

    f.write(tabulate(l))
    f.close()

def calculate_pi_max_precision():
    big_pi=BigNum(precision=12)
    frac_pi=FractionNum()
    dec_pi=DecimalNum()
    getcontext().prec = 100
    f = open(f'data/pi100.txt', 'w')

    l = [['BigNum', '&'] + calculate_two_param(big_pi.pi, 500),
         ['FractionNum', '&'] + calculate_two_param(frac_pi.pi, 500),
         ['DecimalNum', '&'] + calculate_two_param(dec_pi.pi, 500)]

    f.write(tabulate(l))
    f.close()

big = BigNum()
frac = FractionNum()
dec = DecimalNum()
extend = Extended754Num(2, 100, 53, repr_base=10)
# getcontext().prec=100

# calculate_pi(big, frac, dec)
# calculate_e(big, frac, dec)
# calculate_sin(big, frac, dec, 1)
# calculate_sin(big, frac, dec, math.pi)
# calculate_cos(big, frac, dec, math.pi / 2)
# calculate_cos(big, frac, dec, 0)
# calculate_ln(big, frac, dec, math.e)
# calculate_ln(big, frac, dec, 34)
# calculate_sqrt(big,big,dec,2,2)
# calculate_sqrt(big,big,dec,45,12)
# calculate_pow(big,big,dec,3,4.5)
# calculate_pow(big,big,dec,math.pi,0.5)
# calculate_asin(big,frac,dec,1)
# calculate_atan(big,frac,dec,20)
print(dec(6)/dec(10)==dec(3)/dec(5))
print(frac(0.15)*frac(2)==frac(0.1)+frac(0.2))
