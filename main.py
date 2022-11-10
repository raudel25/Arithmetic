import math

import big_num.math
import fraction_num.math
from big_num.numbers import Numbers
import numpy
import decimal
from fixedpoint import FixedPoint
import fractions
a=Numbers('2')


print(big_num.math.ln(a))
print(math.log(2))
s=fraction_num.math.ln(fractions.Fraction(2))

print(s.numerator/s.denominator)



