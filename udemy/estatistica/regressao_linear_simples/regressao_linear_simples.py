#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Objetivo: Com base da distância, fazer uma previsão sobre a velocidade
"""

import pandas as pd #para o carregamento da base
import numpy as np #para calculos matemáticos
import matplotlib.pyplot as plt #para visualização do gráfico
from sklearn.linear_model import LinearRegression #um dos mais utilizados pra trabalhar com machine learning
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('cars.csv') #lendo o csv
base = base.drop(['Unnamed: 0'], axis = 1) #excluindo primeira coluna, pois não será usada (axis = 1, significa que quero apagar por coluna)

X = base.iloc[:, 1].values #X é a variável independente, a distância (todas as linhas da coluna 1)
X_reshaped = X.reshape(-1, 1) #vai reformular o X para ficar em formato de matriz, e pode usar na regressão linear

y = base.iloc[:, 0].values #y é a variável dependente, a velocidade, que eu desejo prever

correlacao = np.corrcoef(X, y) #corrcoef = coeficiente de correlação

modelo = LinearRegression()
modelo.fit(X_reshaped, y) #usado para fazer o treinamento

interceccao = modelo.intercept_ #intercecção
inclinacao = modelo.coef_ #inclinacao

plt.scatter(X_reshaped, y) #para plotar o grafico
plt.scatter(X_reshaped, modelo.predict(X_reshaped), color = 'red') #passando os dados e os as previsões dos dados, ele traçará a linha de melhor ajuste (ou linha de regressão)

"""
exercicio:
    Para uma distância de 22, qual a velocidade prevista?
"""

distancia = 22

#Forma 1:
previsao_metodo_1 = modelo.intercept_ + modelo.coef_ * distancia
#Forma 2
previsao_metodo_2 = modelo.predict(distancia)

#residuais (distancia entre os pontos da tua base de dados, para a linha de regressão)
residuais = modelo._residues #gerado através da sklearn, e não mostra o valor de resíduo de cada ponto. Caso deseje esses valores individuais, devemos usar a biblioteca yellowbrick

"""
usando a biblioteca yellowbrick
"""
visualizador = ResidualsPlot(modelo)
visualizador.fit(X_reshaped, y)
visualizador.poof() #metodo para visualizar o grafico