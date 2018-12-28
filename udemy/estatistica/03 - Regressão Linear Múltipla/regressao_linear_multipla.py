#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Regressão Linear Múltipla
"""

import pandas as pd #para o carregamento da base
import numpy as np #para calculos matemáticos
import matplotlib.pyplot as plt #para visualização do gráfico
from sklearn.linear_model import LinearRegression #um dos mais utilizados pra trabalhar com machine learning
import statsmodels.formula.api as sm #serve para gerar modelos no python, como se estivesse escrevendo código no R

base = pd.read_csv('mt_cars.csv') #lendo o csv
base = base.drop(['Unnamed: 0'], axis = 1) #excluindo primeira coluna, pois não será usada (axis = 1, significa que quero apagar por coluna)

"""
inicialmente uma regressão simples entre consumo e as polegadas dos veículos
"""

X = base.iloc[:, 2].values #coluda do disp, q representa as polegadas
y = base.iloc[:, 0].values #coluna do mpg, q representa o consumo

correlacao = np.corrcoef(X, y) #deu -0.847, ou seja uma correlação relativa forte. Enquanto o X aumenta, o y diminui

#necessário para formatar de tal modo que possa ser usado pela biblioteca do sklearn LinearRegression
X = X.reshape(-1, 1) #-1 porque não vai alterar nada no eixo, e 1 porque vai auto preencher o eixo

modelo = LinearRegression()
modelo.fit(X, y)

intercept = modelo.intercept_ #termo independente no modelo linear
inclinacao = modelo.coef_ #inclinação

"""
Forma de visualizar o Rˆ2, que indica o quanto as variáveis independentes explicam a variável dependente
"""
R2 = modelo.score(X, y)


previsoes = modelo.predict(X)
#mpg e disp são os nomes das colunas
R2_ajustado = sm.ols(formula = 'mpg ~ disp', data = base)  #ordinary least square (que é um tipo de regressão)
modelo_treinado = R2_ajustado.fit()
modelo_treinado.summary()

"""
visualização do grafico
"""
plt.scatter(X, y)
plt.plot(X, previsoes, color= 'red')


"""
Regressão multipla entre consumo e as cilidradas, as polegadas dos veículos e no hp (que é o número de cavalos)
"""

X1 = base.iloc[:, 1:4].values #do atributo 1 até o atributo 4 (4 não é incluído)
y1 = base.iloc[:, 0].values

modelo2 = LinearRegression()
modelo2.fit(X1, y1)

modelo2.score(X1, y1)
#mpg, cyl, disp e hp são os nomes das colunas
R2_ajustado_2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)  #ordinary least square (que é um tipo de regressão)
modelo_treinado_2 = R2_ajustado_2.fit()
modelo_treinado_2.summary()

novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
modelo2.predict(novo)