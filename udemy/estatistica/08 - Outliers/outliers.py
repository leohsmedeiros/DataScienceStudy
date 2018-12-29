#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN #para detectar outliers usando o método KNN

iris = pd.read_csv('iris.csv')

"""
Para fazer a identificação dos outliers, vamos usar o atributo (coluna) 'sepal width'
"""

#iloc para pegar somente uma parte da base
#iloc[:, 1] : lê-se, todas as linhas, da coluna 1
#os pontos na parte superior, e inferior do gráfico gerado, são os valores considerados outliers
#plt.boxplot(iris.iloc[:, 1], showfliers = False) : showfliers = False, vai ocultar os outliers do grafico
plt.boxplot(iris.iloc[:, 1])

"""
caso queira extrair os outliers
"""

#os valores 4.0 e 2.1 foram identificados pelo grafico
#sepal width: coluna extraída
#|: representa condição 'or'
outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1)]

sepal_width = iris.iloc[:, 1].values
sepal_width = sepal_width.reshape(-1, 1)
detector = KNN()
detector.fit(sepal_width)

"""
em previsões:
    - 1: são outliers
    - 0: NÃO são outliers
"""
previsoes = detector.labels_




