#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import poisson

"""
P(X = x)

Exemplo 1:
    O número de acidente de carros que ocorrem por dia é 2.
    Qual a probabilidade de ocorrerem 3 acidentes no dia?
"""

resposta_exemplo_1 = poisson.pmf(3, 2)

"""
P(X < x)

Exemplo 2:
    O número de acidente de carros que ocorrem por dia é 2.
    Qual a probabilidade de ocorrerem 3 ou MENOS acidentes no dia?
"""

resposta_exemplo_2 = poisson.cdf(3, 2)

"""
P(X > x)

Exemplo 3:
    O número de acidente de carros que ocorrem por dia é 2.
    Qual a probabilidade de ocorrerem MAIS de 3 acidentes no dia?
"""

resposta_exemplo_3 = poisson.sf(3, 2)


