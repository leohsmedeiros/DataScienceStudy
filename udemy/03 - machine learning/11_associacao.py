#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from apyori import apriori


dados = pd.read_csv('transacoes.txt', header = None)

#pra utilizarmos esses valores vamos precisar fazer uma transformação nesses DataFrames
transacoes = []

#temos 6 registros (percorrer linha a linha)
for i in range(0, 6):
    #esta adicionando dentro da lista transações
    transacoes.append([str(dados.values[i,j]) for j in range(0,3) ])

regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5)

#maneira de ver os resultados
resultados = list(regras)

#uma segunda maneira de ver os resultados
resultados2 = [list(x) for x in resultados]

#uma terceira maneira de ver os resultados
resultados3 = []
for j in range(0, 7): #pq retornou 7 regras
    resultados3.append([list(x) for x in resultados2[j][2]])






