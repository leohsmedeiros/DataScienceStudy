#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from scipy import stats

import statsmodels.api as sm #para usar o anova_lm e o tukeyhsd

from statsmodels.formula.api import ols #para usar o anova_lm
#para utilizar o teste de Turkey
from statsmodels.stats.multicomp import MultiComparison #util para fazer uma comparação entre os atributos


"""
O ALFA DEFAULT É 0.05 (utilizado na maioria das análises)
"""


tratamento = pd.read_csv("anova.csv", sep = ";")

"""
Neste exemplo nosso resultado será as horas, ou seja, quanto tempo
o medicamento levou pra fazer efeito
"""

#inicialmente vamos visualizar um boxplot
tratamento.boxplot(by = 'Remedio', grid = False) #by para fazer um agrupamento e grid false, para retirar as linhas de grade

"""
#com a imagem gerada, podemos concluir:
    - que a mediana do remedio A e do remedio B é a mesma
    - o A tem uma distribuição mais homogênea, pq a caixa do boxplot está mais central
    - o remédio B já tem uma concentração mais pra baixo
    - e para o remédio C uma concentração um pouco mais pra cima
"""

#pra fazermos a aplicação do método Anova, vamos precisar utilizar o método ols (método de regressão)
modelo1 = ols('Horas ~ Remedio', data = tratamento).fit() #variável independente é remedio e variável de resposta é horas

#o mais importante no resultados1 é o resultado em [0, 4], onde vc pode comparar o valor de PR(>F), se é maior que o alfa escolhido
resultados1 = sm.stats.anova_lm(modelo1)

"""
Pra gnt fazer um teste utilizando 2 atributos:    
"""

modelo2 = ols("Horas ~ Remedio * Sexo", data = tratamento).fit() #usando Remedio e Sexo como variáveis independentes
resultados2 = sm.stats.anova_lm(modelo2)
#agora nos resultados, temos um p value (PR(>F)) para Remedio, outro para Sexo e outro para a combinação entre eles

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd() #tukeyhsd q efetivamente vai fazer o teste

#mostrará a comparação entre todos os grupos
print(resultado_teste)

"""
será mostrado:
    - a média da diferença (meandiff);
    - o valor mínimo (lower);
    - o valor máximo (upper);
    - e o reject, que indica se vc vai ou não rejeitar a hipótese nula
"""

#para visualizarmos o gráfico
resultado_teste.plot_simultaneous()
