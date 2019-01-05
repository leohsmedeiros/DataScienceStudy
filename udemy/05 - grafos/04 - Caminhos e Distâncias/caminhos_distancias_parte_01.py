#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot

"""
    Vamos trabalhar com o cálculo dos caminhos e distâncias
"""

grafo = Graph(edges = [(0,2), (0,1), (1,4), (1,5), (2,3), (6,7), (3,7), (4,7), (5,6)], directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

#edge_label vai colocar o valor dos pesos em cada aresta
plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

#vamos calcular a menor rota entre o A -> H
#vpath indica os caminhos dos vertices
caminho_vertice = grafo.get_shortest_paths(0, 7, output = 'vpath')

#por que estamos em uma lista de array com uma única posição
for n in caminho_vertice[0]:
    print(grafo.vs[n]['label'])

#epath indica os caminhos das arestas
#vai retornar o indice do peso de cada aresta percorrida, a soma dos valores nesses indices é a menor distância (custo)
caminho_aresta = grafo.get_shortest_paths(0, 7, output = 'epath')

#o retorno de caminho_aresta é uma matriz, vamos convertê-la manualmente para uma lista
caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)
    
distancia = 0
for e in grafo.es:
    #se o indice do grafo estiver em caminho_aresta_id
    if e.index in caminho_aresta_id:
        distancia += grafo.es[e.index]['weight']
