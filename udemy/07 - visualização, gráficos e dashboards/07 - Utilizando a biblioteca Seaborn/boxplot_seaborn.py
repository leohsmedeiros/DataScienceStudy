#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as srn

"""
    Vamos ver como gerar o gráfico usando a biblioteca Seaborn
"""

base = pd.read_csv('../Arquivos/trees.csv')

srn.boxplot(base.Volume).set_title('Árvores')

#data é quando vc vai trabalhar com a base de dados inteira
srn.boxplot(data = base)