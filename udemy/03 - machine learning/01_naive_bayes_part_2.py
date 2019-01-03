#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

#para contabilizar a taxa de erro e gerar a matrix de confusão
from sklearn.metrics import confusion_matrix, accuracy_score


"""
OBJETIVO:
    utilizar a base de dados Credit.csv para prever se o cliente é um bom ou um mal pagador,
    para saber se o gerente do banco pode ou não emprestar dinheiro ao cliente, usando machine learning
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

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

naive_bayes = GaussianNB()

#X_treinamento são as variáveis independentes da base de dados que vai ser utilizada pra treinar o modelo
#y_treinamento são as variáveis de resposta
naive_bayes.fit(X_treinamento, y_treinamento)

#vai pegar cada um dos registros de X_teste, vai submeter ao modelo já treinado, tabela de probabilidade
#e então vai classificar se cada um desses registros pertencem a classe good ou bad

previsoes = naive_bayes.predict(X_teste)

"""
como foi constatado na comparação entre previsões e y_teste, há algumas previsões que vieram com erro (isso é comum)
precisamos agora contabilizar essa taxa de erros
"""

confusao = confusion_matrix(y_teste, previsoes)

#obtivemos 71% de acerto com esse algoritmo
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto


"""
como na matrix de confusão gerada pela confusion_matrix da sklearn não conseguimos distinguir os valores pra good e bad,
vamos importar a ConfusionMatrix da yellowbrick e gerar uma nova matriz de confusão

no resultado lê-se:

    ------------------------------------------------------------
    | bad classificado como bad  | bad classificado como good  |
    ------------------------------------------------------------
    | good classificado como bad | good classificado como good |
    ------------------------------------------------------------

"""

from yellowbrick.classifier import ConfusionMatrix

visualizador = ConfusionMatrix(GaussianNB())
visualizador.fit(X_treinamento, y_treinamento)
visualizador.score(X_teste, y_teste)
visualizador.poof() #para visualizar
