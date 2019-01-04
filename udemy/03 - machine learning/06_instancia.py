#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets #carregando base de dados do sklearn
from scipy import stats #para visualizarmos algumas estatisticas


iris = datasets.load_iris()

#para visualizarmos valores estatísticos, como valor máximo, mínimo, variância, média, etc
stats.describe(iris.data)

previsores = iris.data
classe = iris.target

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

#tem que passar o número de vizinhos mais próximos
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_treinamento, y_treinamento)

"""
LEMBRANDO:
    o treinamento no KNeighborsClassifier é diferente dos outros algoritmos estudados,
    como o naive bayes, arvores de decisão, etc.
    Pois aqueles algoritmos geram efetivamente um modelo. Por exemplo, o naive bayes, quando
    você faz o treinamento ele gera uma tabela de probabilidade, quando quiser classificar um
    novo registro ele usa essa tabela. Assim como a árvore de decisão (que gera uma árvore) e o
    svm (que estudamos em seleção de atributos).
    Já neste tipo de algoritmo o treinamento é simplesmente armazenar os valores, e quando eu quiser
    fazer uma classificação, ele vai simplesmente fazer uma comparação da distância com esses
    registros já armazenados

"""

previsoes = knn.predict(X_teste) #gerou as classificações na classe 0, 1 e 2

#pela diagonal principal fica bem claro que teve um alto número de acertos
#na verdade errou só 1 valor que esta em [1:2] (o resultado deveria ser 0, nesta posição)
confusao = confusion_matrix(y_teste, previsoes)

#taxa de acerto: 0.9777777777777777 ou 97.7%
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto
