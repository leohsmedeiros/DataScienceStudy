#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


base = pd.read_csv('../Arquivos/trees.csv')

#é feito variável por variável

#perceba que temo um outlier em cima
"""
    Parâmetros:
        - showfliers: visualizar os outliers
        - vert: para colocar na vertical ou na horizontal
        - notch: destaca a mediana
        - patch_artist: para deixar ele todo pintado
"""
plt.boxplot(base.Volume, vert = False, showfliers = True, notch = True, patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')

#para colorir o boxplot:
#https://matplotlib.org/gallery/statistics/boxplot_demo.html

#para gerar o boxplot de toda a base
plt.boxplot(base)

plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)
plt.boxplot(base.Volume, vert = False)







