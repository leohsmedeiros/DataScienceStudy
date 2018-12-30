#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#tsa vem de Time Series Analisys
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('AirPassengers.csv')
dateFormat = '%Y-%m'
dateparse = lambda dates: pd.datetime.strptime(dates, dateFormat)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
time_series = base['#Passengers']
                   
plt.plot(time_series)

decomposicao = seasonal_decompose(time_series)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid #random ou residuo


#podemos concluir: as quedas que podemos observar no grafico do time_series provavelmente vieram por conta da sazonalidade
plt.plot(sazonal)
#podemos concluir: o crescimento que podemos observar no grafico do time_series provavelmente vieram por conta da tendencia
plt.plot(tendencia)
#podemos concluir: o aleatorio é o que sobrou da tendencia e do elemento sazonal
plt.plot(aleatorio)

"""
AGRUPAR OS GRAFICOS USANDO SUBPLOT

subplot parameters:
    first: quantidade de graficos que serão plotados (pra dar um efeito parecido com 1 grafico por linha)
    second: tamanho do grafico (quanto maior o valor, menor o grafico) (como se criasse uma nova coluna)
    third: id (se tiverem chamadas com valores iguais, ele vai sobrescrever)
"""

plt.subplot(4, 1, 1)
plt.plot(time_series, label = 'Original')
plt.legend(loc = 'best') #loc para informar a localização (best ele vai ajustar no melhor local para visualizar)

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best') #loc para informar a localização (best ele vai ajustar no melhor local para visualizar)

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best') #loc para informar a localização (best ele vai ajustar no melhor local para visualizar)

plt.subplot(4, 1, 4)
plt.plot(aleatorio, label = 'Aleatorio')
plt.legend(loc = 'best') #loc para informar a localização (best ele vai ajustar no melhor local para visualizar)

#OPCIONAL: para reposicionar melhor (caso um grafico esteja sobreposto a outro)
plt.tight_layout()










