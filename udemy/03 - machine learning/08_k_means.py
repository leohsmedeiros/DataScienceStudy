#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#carregando dados do dataset iris, do sklearn
iris = datasets.load_iris()

#vamos fazer uma contagem de quantos elementos nós temos de cada classe
unicos, quantidade = np.unique(iris.target, return_counts = True)

"""
Perceba que ele trouxe dois vetores, para a classe 0 temos 50,
pra classe 1 também 50 e pra classe 2 também

Então nosso objetivo agora é utilizar o algoritmo de agrupamento, vamos passar
os dados e ver se ele vai conseguir fazer o agrupamento em configurações
parecidas com essa que nós temos originalmente na base de dados
"""

cluster = KMeans(n_clusters = 3) #tem que definir quantos clusters vc quer
cluster.fit(iris.data)

#traz 3 registros, que equivalem a quantidade de clusters
#são 3 centroides e cada linha possui os dados de cada centroide
centroides = cluster.cluster_centers_

previsoes = cluster.labels_

unicos2, quantidade2 = np.unique(previsoes, return_counts = True)

resultados = confusion_matrix(iris.target, previsoes)

#só plotaremos o gráfico com o primeiro e o segundo atributo, por que senão precisaríamos de um grafico 3D ou superior pra mostrar mais atributos

plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1],
            c = 'green', label = 'Setosa')

plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1],
            c = 'red', label = 'Versicolor')

plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1],
            c = 'blue', label = 'Virgica')

plt.legend()