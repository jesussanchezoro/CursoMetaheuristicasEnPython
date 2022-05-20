import pandas as pd
import numpy as np

# Si data es un ndarray entonces el vector de índices debe tener
# la misma longitud que el array de entrada, si no dará error.
serie_1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(serie_1)

# El atributo index guarda el vector de etiquetas para cada
# valor de la serie
print(serie_1.index)
print(serie_1.keys())
print(serie_1.values)

# Si no se proporciona un vector de índices, entonces se crea
# uno automáticamente con los índices numéricos
serie_2 = pd.Series(np.random.rand(5))
print(serie_2)

#La diferencia entre un array de la clase ndarray y una serie de la clase Serie es que en los objetos de clase Serie
# podemos definir de forma explícita el índice de cada elemento, que además puede ser no secuenciales o no contiguos.
serie_3 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
print(serie_3)

# Definición de una serie a partir de un diccionario
d = {'a': 1., 'b': 2., 'c': 3.0, 'd': 4. }
pd.Series(d)

# Si data es un diccionario, entonces si pasamos un vector de
# índices se usará para tomar los elementos del diccionario de
# datos que se correspondan con las etiquetas proporcionadas,
# en el mismo orden que indique el vector de índices
# En caso de que algún índice no tenga valor, pondrá NaN
pd.Series(d, index = ['e', 'd', 'c', 'f', 'b', 'a'])

#Como decíamos al principio, también podemos construir una Serie a partir de un valor escalar.
# En este caso debe especificarse un array de índices y el valor escalar se repetirá tantas veces como índices haya.

pd.Series(3.5, index=['a', 'b', 'c', 'd'])

# Finalmente, también podemos poner un nombre a la serie de valores
# y de índices con los argumentos name e index.name
serie_2.name = "Serie 2"
serie_2.index.name = "Ordinal"
serie_2
