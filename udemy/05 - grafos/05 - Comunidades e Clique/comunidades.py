#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot
import igraph
import numpy as np

"""
    COMUNIDADES

    exemplo 1
"""

grafo = igraph.load('Grafo.graphml')
print(grafo)

plot(grafo, bbox = (300, 300))

#para identificarmos as comunidades, ou seja aquelas que estão próximas umas das outras
comunidades = grafo.clusters()
print(comunidades)
#pra qual comunidade cada integrante foi vinculado
comunidades.membership

plot(grafo, vertex_color = comunidades.membership)

"""
    exemplo 2
"""

grafo2 = Graph(edges = [(0,2), (0,1), (1,4), (1,5), (2,3), (6,7), (3,7), (4,7), (5,6)], directed = True)
grafo2.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo2.es['weight'] = [2,1,2,1,2,1,3,1]

plot(grafo2, bbox = (300,300))

comunidades2 = grafo2.clusters()
print(comunidades2) #colocou cada um em um grupo
comunidades2.membership

#gera um dendrograma (agrupamento hierárquico)
c = grafo2.community_edge_betweenness()
print(c)
#por meio do dedrograma ele vai calcular o número otimo de grupos (no caso retornou 3)
c.optimal_count
comunidades3 = c.as_clustering()
print(comunidades3)
comunidades3.membership

#esta usando membership para atribuir a cor, mas o membership varia de 0 a 2 e em RGB são variações de preto imperceptíveis ao olho humano
plot(grafo2, vertex_color = comunidades3.membership)

#vamos modificar para que sejam cores distintas
cores = comunidades3.membership
#vamos converter para numpy array para podermos fazer uma multiplicação
cores = np.array(cores)
cores = cores * 100
#caso o plot tenha problema em ler direto de um numpy array, fazemos a conversão para lista
cores = cores.tolist()

plot(grafo2, bbox = (300,300), vertex_color = cores)


"""
    CLIQUES
"""

#precisamos transforma-lo em um grafo não direcionado
cli = grafo.as_undirected().cliques(min = 4)
print(cli)
len(cli)
