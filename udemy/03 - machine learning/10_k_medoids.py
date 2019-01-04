#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer


"""
    Uma coisa que será feita de diferente, é que vamos trabalhar somente com o
    agrupamento dos atributos 0 e 1, pq com essa função 'cluster_visualizer',
    podemos visualizar apenas dois grupos.
"""


iris = datasets.load_iris()

#[3, 12, 20] são indices aleatórios, não faz muita diferença trocar esses valores
cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster.get_medoids()
cluster.process() #para fazer o agrupamento
previsoes = cluster.get_clusters() #lista com o resultado
medoids = cluster.get_medoids()

visualizer = cluster_visualizer()
visualizer.append_clusters(previsoes, data = iris.data[:, 0:2])
#vai marcar os medoids com * (ou uma estrela), e markersize pra indicar o tamanho
visualizer.append_cluster(medoids, data = iris.data[:, 0:2], marker = '*', markersize = 15)
visualizer.show()

lista_previsoes = []
lista_real = []

#vai percorrer o primeiro indice de previsoes e verificar qual é o valor correspondente na outra matriz
for i in range(len(previsoes)):
    for j in range(len(previsoes[i])):
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])

#agora vamos transformar as duas listas no formato do numpy array
#é necessário fazer essa conversão pq vamos utilizar a matriz de confusão
lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)

resultados = confusion_matrix(lista_real, lista_previsoes)
