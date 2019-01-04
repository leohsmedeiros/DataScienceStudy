#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

"""
    Vamos fazer uma implementação usando o algoritmo C-MEANS, para clusterização,
    e neste tipo de algoritmo pode-se definir que os registros podem estar
    alocados em mais de um grupo (agrupamento parcial difuso).

    Então vamos ter como resultado a probabilidade de cada um dos registros
    pertencerem a cada um dos grupos (diferente do algoritmo k-mean, que indica
    o grupo específico do registro)
"""

iris = datasets.load_iris()

"""
    Nesta função (cmeans) não há valor default, então é preciso passar todos
    os parâmetros.
    
    Parâmetros:
        - data: o conjunto de dados (T indica que vamos pegar a matriz
        transposta (oque é linha vira coluna e oq é coluna vira linha))
        - c: número de clusters
        - m: é relacionado ao membership, ou seja a qual grupo cada cluster
        pertence (vamos colocar 2 pq é o valor default, recomendado pela
        documentação)
        - error: é um critério de parada (0.005 é um valor default, recomendado
        pela documentação)
        - maxiter: quantas vezes ele vai iterar (fazer a repetição)
        - init: Matriz inicial c-particionada fuzzy. Se colocado 'None', o
        algoritmo é inicializado randômicamente.        
"""

resultado = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2, error = 0.005,
                           maxiter = 1000, init = None) 

"""
    Conclusões sobre o resultado:
        
    - o resultado é uma tupla com 7 posições, mas oque nos interessa é o index 1
    - por termos pego a matriz transposta, cada coluna equivale a um registro e
    cada linha equivale a probabilidade de fazer parte de um determinado grupo
    (grupo 0, 1 ou 2)
    
"""

previsoes_porcentagem = resultado[1]
previsoes_porcentagem[0][0] #probabilidade de o registro 0 estar no grupo 0
previsoes_porcentagem[1][0] #probabilidade de o registro 0 estar no grupo 1
previsoes_porcentagem[2][0] #probabilidade de o registro 0 estar no grupo 2

#vai pegar o índice do maior valor entre as linhas da coluna 0
previsoes = previsoes_porcentagem.argmax(axis = 0) 
resultados = confusion_matrix(iris.target, previsoes)

