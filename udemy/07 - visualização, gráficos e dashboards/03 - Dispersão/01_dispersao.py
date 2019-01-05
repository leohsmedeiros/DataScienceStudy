#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
    Gráfico de dispersão para verificarmos se existe uma relação entre variáveis
    contínuas
    
    Vamos então analisar a relação entre a variável Girth (circunferência) e a
    variável Volume da árvore (carregada na base)
"""

base = pd.read_csv('../Arquivos/trees.csv')

#facecolors tira o preenchimento dos markers
#na documentação há todos os markers possíveis
plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')

#podemos tbm visualizar um Grafico de linha
plt.plot(base.Girth, base.Volume)

#para poder visualizar pontos sobrepostos

#x_jitter (e y_jitter) é para afastar (apenas visualmente) pontos sobrepostos

#fit_reg é para mostrar ou ocultar a linha de regressão
sns.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.1, fit_reg = False)
#é bem similar, mas coloca uma linha de regressão










