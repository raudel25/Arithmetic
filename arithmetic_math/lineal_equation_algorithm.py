from .arithmetic_math import ArithmeticMath

def zeros(arithmetic:ArithmeticMath,n: int):
    l=[]

    for _ in range(n):
        l.append(arithmetic.number0())

    return l

def jacobi(arithmetic:ArithmeticMath,matrix, vector):
    sol = zeros(arithmetic,len(vector))

    for _ in range(1000):
        aux= zeros(arithmetic,len(vector))

        for x in range(len(vector)):
            n=arithmetic.number0()

            for y in range(len(vector)):
                if x == y:
                    continue

                n += -matrix[x][y]*sol[y]

            aux[x] = (n+vector[x])/matrix[x][x]

        for x in range(len(vector)):
            sol[x] = aux[x]


    return sol


def gauss_seidel(arithmetic:ArithmeticMath,matrix, vector):
    sol=zeros(arithmetic,len(vector))

    for _ in range(1000):
        aux=zeros(arithmetic,len(vector))
        mask: list = [False for _ in range(len(vector))]

        for x in range(len(vector)):
            n=arithmetic.number0()

            for y in range(len(vector)):
                if x == y:
                    continue

                if mask[y]:
                    n += -matrix[x][y]*aux[y]
                else:
                    n += -matrix[x][y]*sol[y]

            aux[x] = (n+vector[x])/matrix[x][x]
            mask[x] = True

        for x in range(len(vector)):
            sol[x] = aux[x]

    return sol
