from big_num.numbers import Numbers


def constant_e(precision: int , precision_decimal: int,number1,number0_precision):
    e=number0_precision
    fact: 'Numbers' = number1
    index = number0_precision

    # Formula de taylor e^x
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        e += number1 / fact
        index += Numbers.real1()

    return e
