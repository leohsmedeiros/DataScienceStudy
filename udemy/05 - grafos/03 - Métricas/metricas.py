#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot
import igraph


"""
    Vamos estudar algumas métricas, a partir do grafo carregado em Grafo.graphml
"""

grafo = igraph.load('Grafo.graphml')
print(grafo)

plot(grafo, bbox = (300,300))

grafo.degree(type = 'all') #grau do grafo tanto para entrada, quanto para saída
grafo.degree(type = 'in') #grau de entradas do grafo
grafo.degree(type = 'out') #grau de saídas grafo

#cada posição, na variável, grau é um vértice e indica quantos outros nós apontam para ele
grau = grafo.degree(type = 'in')
plot(grafo, vertex_size = grau)

#vamos fazer um teste com o diâmetro do grafo
#usado para medir qual a maior distância que existe entre os vértices
#quando temos um grafo direcionado, temos os chamados caminhos obrigatórios (as vezes vai para um nó que não tem como voltar)
grafo.diameter(directed = True)

#vai retornar os vértices que tem a maior distância entre os pontos do grafo (interessante para ver qual é o maior caminho)
grafo.get_diameter()

#vizinhança
grafo.neighborhood()

#vamos identificar os grafos isomórficos (aqueles q possuem a mesma estrutura)
grafo2 = grafo
grafo.isomorphic(grafo2) #retornou True, logo os dois grafos são iguais

