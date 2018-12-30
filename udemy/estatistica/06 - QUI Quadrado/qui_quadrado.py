#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import chi2_contingency

"""
Tabela para aplicar o qui quadrado:

----------------------------------------
|           |  Assiste  |  Não Assiste |
| Masculino |     19    |     06       |
| Feminino  |     43    |     32       |
----------------------------------------

"""

novela = np.array([[19, 6], [43, 32]])
contingency = chi2_contingency(novela)
"""
Palavras do professor:
    Oque mais interessa, neste caso, é o segundo parâmetro, que é o valor de P (que no caso é 0.1534...).
    Então como este valor, é maior que o alpha de 0.05 então quer dizer que nós não podemos
    rejeitar a hipótese nula. Neste caso, não há diferença significativa, além do acaso.
"""