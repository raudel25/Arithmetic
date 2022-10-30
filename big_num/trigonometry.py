from .numbers import Numbers


def sin_cos(x: 'Numbers', sin: bool, precision):
    filter1 = (lambda a: (a & 1) == 0) if sin else (lambda a: (a & 1) != 0)
    filter2 = (lambda a: a % 4 == 1) if sin else (lambda a: a % 4 == 0)

    result: 'Numbers' = Numbers.real0()
    pow_value: 'Numbers' = Numbers.real1()
    fact: 'Numbers' = Numbers.real1()
    index: 'Numbers' = Numbers.real0()

    # Serie de taylor sen x cos x
    # https: // es.wikipedia.org / wiki / Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        if i != 0:
            pow_value *= x

        index += Numbers.real1()

        if filter1(i):
            continue

        result = result + pow_value / fact if filter2(i) else result - pow_value / fact

    return result


def atan_method(x: 'Numbers', precision):
    # arctan(x)+arctan(1/x)=pi/2
    # arctan(1/x)=arccot(x)
    if x.abs > Numbers.real1():
        return constant_pi(100,x.precision) / Numbers("2", "0") - atan_method(Numbers.real1()/x,precision)

    pow_value: 'Numbers' = x
    index: 'Numbers' = Numbers.real1()
    arctan: 'Numbers' = Numbers.real0()
    xx: 'Numbers' = x ** Numbers("2", "0")

    for i in range(1, 2 * precision, 2):
        arctan = arctan + pow_value / index if i % 4 == 1 else arctan - pow_value / index
        pow_value *= xx
        index += Numbers("2", "0")

    return arctan


def asin_method(x: 'Numbers', precision):
    if x.abs > Numbers.real1():
        raise Exception("Operacion Invalida (arcsin recive valores entre 1 y -1)")

    index = Numbers.real1()
    even = Numbers.real1()
    odd = Numbers.real1()
    pow_value = Numbers.real1()
    arcsin = Numbers.real0()

    for i in range(1, precision):
        pow_value *= x

        if (i & 1) == 0:
            even *= index

        if (i & 1) == 1:
            arcsin += (odd * pow_value) / (even * index)
            odd *= index

        index += Numbers.real1()

    return arcsin


def constant_pi(precision,precision_decimal):
    return asin_method(Numbers("0", "5",True,precision_decimal),precision) * Numbers("6", "0")
