#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv('../Arquivos/trees.csv')

#pegamos a altura dessa vez
plt.hist(base.iloc[:, 1], bins = 10)

"""
    Parâmetros:
        - hist: a visibilidade do histograma no fundo
        - kde: a visibilidade do gráfico de densidade
        - color: cor da linha de densidade
"""
sns.distplot(base.iloc[:, 1], bins = 10, hist = True, kde = True, color = 'green')










