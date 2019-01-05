#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


base = pd.read_csv('../Arquivos/trees.csv')

"""
    vamos criar um histograma somente com o atributo Girth.
    
    foi gerado uma lista onde a primeira posição mostra a quantidade de registros
    e a segunda posição mostra o valor desses registros, respectivamente
    
    Lendo o resultado:
        0: [4 2 5 7 9 4]
        1: [63. 67. 71. 75. 79. 83. 87.]
        
        - entre o intervalo de 63 e 67 = 4 registros
        - entre o intervalo de 67 e 71 = 2 registros
        - entre o intervalo de 71 e 75 = 5 registros
        - entre o intervalo de 75 e 79 = 7 registros
        - entre o intervalo de 79 e 83 = 9 registros
        - entre o intervalo de 83 e 87 = 4 registros
"""
histograma = np.histogram(base.iloc[:, 1], bins = 'auto') #bin numero de intervalos (pode ser passado um número manualmente, mas o auto vai dividir de forma automatica)


plt.hist(base.iloc[:,1], bins = 'auto')
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')
