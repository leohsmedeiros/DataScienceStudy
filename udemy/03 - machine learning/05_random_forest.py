#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

"""
    Nesta aula nós vamos fazer uma implementação utilizando o algoritmo 'Random Forest',
    que faz parte da idéia de 'ensemble learning', que é utilizar mais de um classificador
    
    O Kinect utiliza este algoritmo para fazer a classificação dos pontos do corpo
"""

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:, 20].values

labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])

#30% para teste e 70% para treinamento
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

#n_estimators é o número de árvores de decisão que vc quer gerar
floresta = RandomForestClassifier(n_estimators = 100)
floresta.fit(X_treinamento, y_treinamento) #vai gerar as 100 arvores de decisão
previsoes = floresta.predict(X_teste)

confusao = confusion_matrix(y_teste, previsoes)
#taxa de acerto: 0.7733333333333333 ou 77.3%
taxa_acerto = accuracy_score(y_teste, previsoes)

#vai mostrar as 100 árvores de decisão que foram criadas
floresta.estimators_
#para pegar uma das florestas
floresta.estimators_[0]











