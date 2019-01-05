#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

"""
    Vamos ver como colocar vários gráficos na mesma figura
"""

base = pd.read_csv('../Arquivos/trees.csv')

plt.figure(1)

"""
    Parâmetros:
        - (0): número de linhas reservadas pro gráfico (como se fosse uma tabela
        de gráficos)
        - (1): número de colunas reservadas pro gráfico (como se fosse uma tabela
        de gráficos)
        - (2): id do gráfico
"""
#girth com volume
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)

#girth com height
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)

#height com volume
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume)

#histograma com volume
plt.subplot(2,2,4)
plt.hist(base.Volume)
