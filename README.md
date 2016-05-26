##La heurística

Para realizar la implementación de la heurística hemos creado las clases
VerticalHeuristic, HorizontalHeuristic, UpwardHeuristic,
DownwardHeuristic.

Estas clases representan un escaneo completo del tablero para el estado actual.

Básicamente el escaneo consiste en mirar por columnas, (vertical y diagonales) o por filas, (horizontal).
Descartando las casillas vacías, buscando el numero de ocurrencias de "X" o "O" (ocurrences_of()), y comprobando
los laterales de dicha ocurrencia (connection_breaks()), para asignar un valor a cada caso posible y para cada
valor de la ocurrencia.

Los valores de la heuristica, tomando X como jugador problema y O como el otro jugador:


|       | Vertical | Horizontal | Diagonales |
|:-----:|:--------:|:----------:|:----------:|
|     X |    20    |     40     |     50     |
|    XO |    10    |     20     |     25     |
|    OX |     0    |     20     |     25     |
|   OXO |     0    |      0     |      0     |
|    XX |    240   |     400    |     500    |
|   XXO |    120   |     200    |     250    |
|   OXX |     0    |     200    |     250    |
|  OXXO |     0    |      0     |      0     |
|   XXX |    700   |     800    |     900    |
|  XXXO |    350   |     400    |     450    |
|  OXXX |     0    |     400    |     450    |
| OXXXO |     0    |      0     |      0     |
|  XXXX |    inf   |     inf    |     inf    |


|       | Vertical | Horizontal | Diagonales |
|:-----:|:--------:|:----------:|:----------:|
|     O |    -20   |     -40    |     -50    |
|    OX |    -10   |     -20    |     -25    |
|    XO |     0    |     -20    |     -25    |
|   XOX |     0    |      0     |      0     |
|    OO |   -240   |    -400    |    -500    |
|   OOX |   -120   |    -200    |    -250    |
|   XOO |     0    |    -200    |    -250    |
|  XOOX |     0    |      0     |      0     |
|   OOO |   -700   |    -800    |    -900    |
|  OOOX |   -350   |    -400    |    -450    |
|  XOOO |     0    |    -400    |    -450    |
| XOOOX |     0    |      0     |      0     |
|  OOOO |   -inf   |    -inf    |    -inf    |


##Tests

En el directorio /test se encuentran las clases de test unitarios para cada clase, que representan un buen numero
de posibles estados y valores.

##Dificultad

Se ha añadido 3 niveles de dificultad:

* Nivel fácil, profundidad de la busqueda es = 2
* Nivel normal, profundidad de la busqueda es = 3
* Nivel difícil, profundidad de la busqueda es = 4

Seleccionables al iniciar el juego.

##Jugador inicial

Se ha rediseñado el concepto de player para poder empezar como "O" nosotros cambiando solo una variable.


##Memoization

Se ha utilizado la técnica de optimización [memoization](https://en.wikipedia.org/wiki/Memoization) para mejorar el rendimiento de la heuriscitca, que
consiste en guardar en un diccionario la clave y valor de la heuristica para cada estado, de esta forma,
aprovechar las heuristicas ya calculadas para estados iguales.
