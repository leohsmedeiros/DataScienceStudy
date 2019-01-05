#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

base = pd.read_csv('../Arquivos/co2.csv')

#hue faz a criação da legenda e diferencia os pontos, de acordo com o tipo
srn.scatterplot(base.conc, base.uptake, hue = base.Type)

quebec = base.loc[base['Type'] == 'Quebec']
mississippi = base.loc[base['Type'] == 'Mississippi']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(quebec.conc, quebec.uptake).set_title('Quebec')
plt.subplot(1,2,2)
srn.scatterplot(mississippi.conc, mississippi.uptake).set_title('Mississippi')
plt.tight_layout()

#REFRIGERADO E NÃO REFRIGERADO
chilled = base.loc[base['Treatment'] == 'chilled']
nonchilled = base.loc[base['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(chilled.conc, chilled.uptake).set_title('Chilled')
plt.subplot(1,2,2)
srn.scatterplot(nonchilled.conc, nonchilled.uptake).set_title('Non chilled')
plt.tight_layout()


"""
    Vamos carregar outra base de dados para explorarmos o relacionamento entre
    dados categóricos
"""

base2 = pd.read_csv('../Arquivos/esoph.csv')

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')