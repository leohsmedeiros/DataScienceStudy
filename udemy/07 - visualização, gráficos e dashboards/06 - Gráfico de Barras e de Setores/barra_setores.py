#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


base = pd.read_csv('../Arquivos/insect.csv')

#nome do atributo categórico que quero fazer o agrupamento (spray)
#depois coloca no [''] a coluna da base de dados na qual vc quer fazer o somatório (no caso count)
agrupado = base.groupby(['spray'])['count'].sum()

#GRAFICO DE BARRA

#essa função plot não é a do matplotlib, mas sim a do pandas
agrupado.plot.bar(color = 'gray')

#GRAFICO DE SETORES (OU GRAFICO DE PIZZA)
agrupado.plot.pie(legend = True)







