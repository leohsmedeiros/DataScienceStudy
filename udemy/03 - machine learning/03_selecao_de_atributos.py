#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier #vai retornar a importância dos atributos


"""
DESTA VEZ VAMOS USAR O ALGORITMO SVM
e vamos identificar a importância de cada atributo
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

modelo = SVC()
modelo.fit(X_treinamento, y_treinamento)

previsoes = modelo.predict(X_teste)
taxa_acerto = accuracy_score(y_teste, previsoes)

forest = ExtraTreesClassifier()
forest.fit(X_treinamento, y_treinamento)

#vai estar mostrando atributo, por atributo, quais são os mais importantes
#quanto maior o valor, mais significativo o atributo é
importancias = forest.feature_importances_

"""
    Vamos recriar uma estrutura apenas com os atributos da coluna 0, 1, 2 e 3,
    pois são os mais importante, segundo consta em importancias
    
    É aquela idéia estudada, de que as vezes muitos atributos, pode piorar seu modelo.
    Por isso vamos refazê-lo com apenas os atributos mais importântes
    
    
    RESULTADO DAS TAXAS DE ACERTO:
        
        - com todos os atributos:
            0.7133333333333334
        - com apenas os atributos mais relevantes:
            0.7266666666666667
"""

X_treinamento2 = X_treinamento[:, [0,1,2,3]]
X_teste2 = X_teste[:, [0,1,2,3]]

modelo2 = SVC()
modelo2.fit(X_treinamento2, y_treinamento)

previsoes2 = modelo2.predict(X_teste2)

taxa_acerto_2 = accuracy_score(y_teste, previsoes2)
