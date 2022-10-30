from .numbers import Numbers


def constant_e(precision: int , precision_decimal: int):
    e: 'Numbers' = Numbers('0', '0', True, precision_decimal)
    fact: 'Numbers' = Numbers.real1()
    index = Numbers('0', '0', True, precision_decimal)

    # Formula de taylor e^x
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        e += Numbers.real1() / fact
        index += Numbers.real1()

    return e
