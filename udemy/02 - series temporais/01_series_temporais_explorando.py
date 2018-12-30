#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv('AirPassengers.csv')

#a primeira coisa que precisamos fazer é transformar a coluna Month em um tipo data, para usarmos nas funções de series temporais
print(base.dtypes) #mostra o tipo de cada colune ('Passengers' esta no tipo int64 e 'Month' no tipo object)

dateFormat = '%Y-%m'

#strptime (da biblioteca pandas): vai tentar converter o object do Month em um tipo de data
dateparse = lambda dates: pd.datetime.strptime(dates, dateFormat) #lambda function em python

#vamos recarregar o csv, já formatando a coluna Month
#parse_dates: coluna a fazer o parse
#index_col: vai transformar a coluna indica no índice da tabela (pode ser passado em valor numérico )
#date_parser: o parser, que criamos em dateparse
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)

#uma prática recomendada pra trabalhar com série temporal no python, é transformar a base do tipo DataFrame para o tipo Series
time_series = base['#Passengers']

#note que time_series foi gerado no tipo Series
#podemos indexar pelo índice no valor numérico ou pela data
#Exemplo: time_series[1]  ou  time_series['1949-02-01']  ou  time_series[datetime(1949,2,1)]
time_series[datetime(1949,2,1)] #para poder indexar desta forma tivemos que importar o datetime
time_series['1950-01-01' : '1950-07-31'] #vai trazer os valores entre '1950-01-01' e '1950-07-31'
time_series[: '1950-07-31'] #vai trazer todos os valores anteriores até a data '1950-07-31'
time_series['1950'] #traz todos os meses de 1950
time_series.index.max() #traz a maior data (porque esta pegando a partir do atributo index)
time_series.index.min() #traz a menor data (porque esta pegando a partir do atributo index)

plt.plot(time_series) #podemos concluir que houve um crescimento significativo desde 1949 até 1961

#agrupamento por ano
#também pode ser feito dessa forma (o parametro 'A' do resample vem de Ano): time_series_ano = time_series.resample('A').sum()
time_series_ano = time_series.groupby([lambda x: x.year]).sum()
plt.plot(time_series_ano)

#agrupamento por mês
time_series_mes = time_series.groupby([lambda x: x.month]).sum()
plt.plot(time_series_mes)

#agrupamento por datas
time_series_datas = time_series['1960-01-01' : '1960-12-01']
plt.plot(time_series_datas)




