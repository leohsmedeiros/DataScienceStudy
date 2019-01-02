#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regressão Logística
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

#se fosse a vírgula não precisaria passar o parâmetro sep, mas como no csv o separador é o ;, tivemos que fazer essa configuração
base = pd.read_csv('Eleicao.csv', sep = ';')

plt.scatter(base.DESPESAS, base.SITUACAO)
base.describe()

np.corrcoef(base.DESPESAS, base.SITUACAO)

X = base.iloc[:, 2].values
y = base.iloc[:, 1].values

X = X[:, np.newaxis]

modelo = LogisticRegression()
modelo.fit(X, y)

modelo.coef_
modelo.intercept_

plt.scatter(X, y)

X_teste = np.linspace(10, 3000, 100) #linspace vai gerar 100 números aleatórios, variando de 10 a 3000

#função que vai receber um número e retornar a sigmóide
def model(x):
    return 1 / (1 + np.exp(-x))

#ravel vai transformar o numpy array de formato de matriz, para o formato de vetor
r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(X_teste, r, color = 'red')

"""
Agora vamos usar o arquivo NovosCandidatos.csv e fazer previsão para cada um deles
"""

base_previsoes = pd.read_csv('NovosCandidatos.csv', sep = ';')
despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
previsoes_teste = modelo.predict(despesas) #resultado

#criando uma nova tabela, que relaciona o resultado com os dados que tinhamos, pra facilitar a leitura
base_previsoes = np.column_stack((base_previsoes, previsoes_teste))
base_previsoes