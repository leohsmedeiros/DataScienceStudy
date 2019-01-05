#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot

"""
    Nesta aula vamos fazer a impressão do caminho no grafo (vamos colorir os
    vértices e as arestas, pertencentes ao menor caminho)
"""

grafo = Graph(edges = [(0,2), (0,1), (1,4), (1,5), (2,3), (6,7), (3,7), (4,7), (5,6)], directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

caminho_vertice = grafo.get_shortest_paths(0, 7, output = 'vpath')
caminho_aresta = grafo.get_shortest_paths(0, 7, output = 'epath')

caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)


caminho_nome_vertices = []
for n in caminho_vertice[0]:
    caminho_nome_vertices.append(grafo.vs[n]['label'])
    
#vamos percorrer todos os vértices, e se o vértice estiver dentro de caminho_nome_vertices, vamos pintá-lo de verde
for v in grafo.vs:
    if v['label'] in caminho_nome_vertices:
        #color já é uma característica Default do igraph (assim como weight e label)
        v['color'] = 'green'
    else:
        v['color'] = 'gray'

    
#agora, vamos pintar as arestas correspondentes ao menor caminho
for e in grafo.es:
    if e.index in caminho_aresta_id:
        #color já é uma característica Default do igraph (assim como weight e label)
        e['color'] = 'green'
    else:
        e['color'] = 'gray'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    