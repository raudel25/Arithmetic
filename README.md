# Arithmetic

Este proyecto tiene como objetivo evaluar el desempeño de distintas aritméticas
de coma flotante, punto fijo y fracciones racionales, en una comparación con nuestra
aritmética: `BigNum`.

## Dependencias

El proyecto está **python**, para ejecutar el proyecto, solo debe escribir en consola:

```bash
make
```

si estas en linux o ejecutar el archivo `main.py` con su intérprete de **python**.

## Descripción de `BigNum`

El funcionamiento de esta biblioteca se basa en la aritmética de punto fijo manteniendo
una precisión exacta de los lugares decimales que podemos modificar dinámicamente, mientras
tanto en la representación de la parte entera si no contamos con ningún límite, por lo que
dentro de nuestros límites computacionales podemos representar cualquier número.

Esta aritmética modela la representación de los números en potencias de base 10, con lo cual
nos acercaremos más a la precisión de los números con los que habitualmente trabajamos, un ejemplo
clásico de estas aproximaciones consiste en: $0.4\cdot 3$ el cual comparamos con $1.2$ en la aritmética
común de los lenguajes de programación y obtendremos un resultado negativo, debido a la representación
periódica en base 2 de uno de estos números.

Para la optimización de las operaciones en `BigNum` y aprovechándonos de que la aritmética de los enteros
en la computadora es exacta, variamos la base de la aritmética a potencias de 10, siempre y cuando no
no excedan la aritmética entera que suele ser en la mayoría de los casos de 64 bits.

Los algoritmos utilizados para las operaciones básicas son:

- La suma y la substracción usual.
- Multiplicación: Está implementada la multiplicación mediante
  el <a href="https://es.wikipedia.org/wiki/Algoritmo_de_Karatsuba#:~:text=El%20paso%20b%C3%A1sico%20del%20algoritmo,sumas%20y%20desplazamientos%20de%20d%C3%ADgitos.">
  algoritmo de Karatsuba</a>, apoyado en la suma antes definida.
- División: Está implementada mediante el **algoritm_d** el cual se basa en la optimización de la división
  de un número de $n+1$ dígitos por otro de $n$ dígitos.

## Aritméticas utilizadas

Compararemos las siguientes aritméticas:

- Decimal: Está implementada en el módulo **decimal** de **python** contiene implementaciones de aritmética de coma flotante y punto fijo, además de la posibilidad
  representar una cantidad de lugares decimales variable.
- Fracciones Racionales: Está implementada en el módulo **fraction** de **python**, los números de esta aritmética cuentan con dos
  números enteros, el numerador y el denominador.
- BigNum: Aritmética propuesta y descrita anteriormente.

## Descripción de `ArithmeticMath`

Para la comparación de las aritméticas definiremos la clase `ArithmeticMath` con las siguientes operaciones:

- Raíz n-ésima: Para esta operación se trata de aproximar mediante una potencia entera y luego se aproxima mediante el
  siguiente <a href="https://es.frwiki.wiki/wiki/Algorithme_de_calcul_de_la_racine_n-i%C3%A8me">algoritmo</a>.

- Potencia: Para esta operación se busca la fracción que genera el exponente y luego se calcula la raíz y la potencia
  correspondiente.

- Número $\pi$: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de
  la función $arcsin(x)$.

- Número $e$: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de la
  función $e^x$.

- Logaritmo en base e: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">
  Taylor</a> de la
  función $ln(1-x)$, con $|x| \leq 1$, si $|x| > 1$ se utiliza la siguiente identidad $ln({1\over x})=-ln(x)$.

- Logaritmo: Se aproxima mediante la identidad $log(a)(b)={ln(a)\over ln(b)}$, con el cálculo de los logaritmos en base
  $e$ correspondientes.

- Seno: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de la
  función $sin(x)$.

- Coseno: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de la
  función $cos(x)$.

- Arcoseno: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de la
  función $arcsin(x)$.

- Arcocoseno: Se aproxima mediante la identidad $arccos(x)={\pi \over 2}-arcsin(x)$, con el cálculo del arcoseno
  correspondiente.

- Arcotangente: Se aproxima mediante la serie de <a href="https://es.wikipedia.org/wiki/Serie_de_Taylor">Taylor</a> de
  la función $arctan(x)$, con $|x| \leq 1$, si $|x| > 1$ se utiliza la siguiente identidad $arctan(x)={\pi \over 2}-arctan({1 \over x})$.

- Arcocotangente: Se aproxima mediante la identidad $arccot(x)={\pi \over 2}-arctan(x)$, con el cálculo de la
  arcotangente correspondiente.
