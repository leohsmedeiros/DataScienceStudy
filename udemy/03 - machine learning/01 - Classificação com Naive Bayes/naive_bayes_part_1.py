#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

#sklearn.model_selection é o pacote que vamos utilizar na maioria dos algoritmos de machine learning
#train_test_split: já utilizamos para fazer a divisão da base de dados (entre treino e teste), lá no modulo de estatistica, quando fizemos amostragem estratificada
from sklearn.model_selection import train_test_split  

#uma particularidade do GaussianNB é que ele não trabalha com dados categóricos
#neste exemplo checking_status, credit_history e outros atributos são categóricos
#oque vai ser necessário fazer, neste caso, é transformar esses atributos em índices
from sklearn.naive_bayes import GaussianNB

#a LabelEncoder faz essa transformação em índices
from sklearn.preprocessing import LabelEncoder


"""
OBJETIVO:
    utilizar a base de dados Credit.csv para prever se o cliente é um bom ou um mal pagador,
    para saber se o gerente do banco pode ou não emprestar dinheiro ao cliente, usando machine learning
"""

credito = pd.read_csv('Credit.csv')
 
#variaveis previsoras ou variaveis independentes (que vão ser utilizadas para gerar uma previsão)
previsores = credito.iloc[:, 0:20].values #vai pegar todas as linhas, e as colunas da 0 até a 19 (o 20 não é incluso)

#se tentar visualizar 'previsores' através do variable explorer vai dar um erro, pois tem vários dados de tipos diferentes
#se quiser validar, print a primeira linha, com o comando previsores[0]


#classe ou variavel de resposta
classe = credito.iloc[:, 20].values

"""
Convertendo atributos categóricos em atributos numéricos (usando LabelEncoder),
para trabalhar com a biblioteca GaussianNB
"""

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

"""
Depois de convertido, agora podemos usar esses dados no algoritmo naive bayes
"""
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, #variáveis independentes
                                                                  classe, #variáveis respostas
                                                                  test_size = 0.3, #30% da base de dados pro treinamento
                                                                  random_state = 0) #random_state = 0 pra sempre dividir a base de dados da mesma maneira, assim nós, em casa, vamos obter o mesmo resultado que o professor





