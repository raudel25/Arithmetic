def scalate_one(x, number10, number1) -> tuple:
    cant: int = 0

    while x < number1:
        x *= number10
        cant += 1

    return x, cant
