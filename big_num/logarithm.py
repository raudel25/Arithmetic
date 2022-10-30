from .numbers import Numbers
from .constant_e import constant_e


def ln_method(x: 'Numbers', precision):
    # ln(1/x)=-ln(x)
    positive: bool = x.abs > Numbers.real1()
    x = Numbers.real1() / x if positive else x
    x = Numbers.real1() - x

    pow_value: 'Numbers' = x
    index: 'Numbers' = Numbers.real1()
    ln: 'Numbers' = Numbers.real0()

    # Serie de Taylor ln(1-x)
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(1, precision):
        ln += pow_value / index
        pow_value *= x
        index += Numbers.real1()

    return ln if positive else -ln


def log_method(x: 'Numbers', y: 'Numbers', precision: int):
    pow_value: 'Numbers' = Numbers.real1()
    index: int = 0

    while pow_value <= y:
        if pow_value == y:
            return Numbers(str(index), '0')
        pow_value *= x
        index += 1

    return ln_method(x, precision) / ln_method(y, precision)
