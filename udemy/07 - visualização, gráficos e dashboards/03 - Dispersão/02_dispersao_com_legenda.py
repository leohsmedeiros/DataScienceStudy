#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


base = pd.read_csv('../Arquivos/co2.csv')

x = base.conc
y = base.uptake

#set: conjunto dos dados sem repetição de valores
unicos = list(set(base.Treatment))

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])

plt.legend(loc = 'lower right')









