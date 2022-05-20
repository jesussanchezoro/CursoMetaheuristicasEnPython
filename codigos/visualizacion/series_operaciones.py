import pandas as pd
import numpy as np

serie_1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
serie_2 = pd.Series(np.random.rand(5))
serie_3 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])

print(np.log10(serie_2))
# Suma elemento a elemento, fijándonos en las etiquetas
# para efectuar el emparejamiento
print(serie_1 + serie_1)

serie_A = pd.Series({'a':0.1, 'c':0.3, 'd':0.5, 'f':0.7})
print(serie_A)
serie_B = pd.Series({'a':0.8, 'b':0.4, 'd':0.6, 'e':0.1})
print(serie_B)
print(serie_A + serie_B)