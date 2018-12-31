#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agora vamos usar arima para fazermos as previsões
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA


base = pd.read_csv('AirPassengers.csv')
dateFormat = '%Y-%m'
dateparse = lambda dates: pd.datetime.strptime(dates, dateFormat)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
time_series = base['#Passengers']
                   
plt.plot(time_series)

"""
parametros:
    - p: número dos termos autoregressivos
    - q: número da média móvel
    - d: número de diferenças não sazonais
    
estes parâmetros tem que ser encontrados por meio de ajustes.
Ou então pode usar o autoarrima, para calcular os melhores valores (usando a biblioteca pyramid)

OBS: não foi possível instalar a biblioteca pyramid arima
comando 'pip install pyramid-arima' estava dando erro, e não encontrei uma solução ainda
"""
modelo = ARIMA(time_series, order = (2, 1, 2))
modelo_treinado = modelo.fit()
modelo_treinado.summary()

#steps vai informar quantas previsões pra frente desejamos fazer
#retorna uma tupla, e as previsões estão no índice 0
previsoes = modelo_treinado.forecast(steps = 12)[0]

"""
PARA PLOTAR UM GRAFICO
"""
eixo = time_series.plot()
#parametro ax representa o eixo, na prática vai simplesmente unir os dois gráficos
modelo_treinado.plot_predict('1960-01-01', '1962-01-01', ax = eixo, plot_insample = True)

#perceba que quanto maior o tempo de previsão a tendência é ficar mais linear
modelo_treinado.plot_predict('1960-01-01', '1970-01-01', ax = eixo, plot_insample = True)


