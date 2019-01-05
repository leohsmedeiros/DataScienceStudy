#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

base = pd.read_csv('../Arquivos/orchard.csv')

figura = plt.figure()

#estamos adicionando um subplot dentro da figura e armazenando em eixo
eixo = figura.add_subplot(1, 1, 1, projection = '3d') #ou seja, 1 linha, 1 coluna e o id do gráfico é 1
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')

#como mudar as cores no gráfico 3d:
#https://pythonspot.com/3d-scatterplot/
