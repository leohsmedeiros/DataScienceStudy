#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

base = pd.read_csv('AirPassengers.csv')
dateFormat = '%Y-%m'
dateparse = lambda dates: pd.datetime.strptime(dates, dateFormat)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
time_series = base['#Passengers']
                   
plt.plot(time_series)

"""
FORMAS DE FAZER PREVISÕES

- quando trabalhamos com previsões fazemos previsões para o futuro
(para além do que temos de dados), significa que vamos extrapolar o conjunto de dados
"""


"""
MANEIRA MAIS FACIL:
    
- a maneira mais facil de fazer previsão é utilizando uma média, porém tem grandes chances de erro,
pois essa média tem uma tendência, ou seja ela não é estacionária, portanto neste caso quando
utilizamos a média, o período em que nós não tinhamos tantos dados, acabam influênciando os períodos
atuais
"""
time_series.mean()


"""
OUTRA MANEIRA

- pegando a média do último ano, que é um pouco mais interessante, pq é um valor um pouco mais parecido
com a atualidade
"""
time_series['1960-01-01' : '1960-12-01'].mean()

"""
OUTRA MANEIRA (Conceito um pouco mais avançado)

- utilizando as médias móveis, que vai considerar n elementos antes dele fazer a previsão
"""
#window quantas 'janelas', ou seja, quantas datas anteriores que vamos utilizar
#por conta do window ser 12, para gerar um valor ele vai analisar através dos 12 valores anteriores
#neste exemplo retornará 12 valores nan, pois não temos os valores anteriores
media_movel = time_series.rolling(window = 12).mean() 
time_series[0:12].mean()
time_series[1:12].mean()

plt.plot(time_series)
plt.plot(media_movel, color = 'red') #note que neste caso ele começa a desenhar em vermelho, 12 pontos depois


#para prever para a proxima data, vamos pegar os últimos 12 meses do conjunto de dados que nós possuímos
previsoes = [] # lista

#vamos gerar previsões para os próximos 12 meses
for i in range(1, 13): # i<13, ou seja de 1 a 12
    superior = len(media_movel) - i #indices
    inferior = superior - 11 #indices
    previsoes.append(media_movel[inferior:superior].mean())

#está em ordem inversa, pq começamos pelo indice superior e fomos descendo
previsoes = previsoes[::-1] #ordenar ao inverso

plt.plot(previsoes)



