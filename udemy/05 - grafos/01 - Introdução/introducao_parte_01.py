#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    To install igraph on MacOS: http://igraph.wikidot.com/installing-python-igraph-on-mac-os-x
    
    para funcionar a visualização do grafo (plot):
        - Tive que substituir o arquivo __init__.py por essa versão:
            https://github.com/igraph/python-igraph/blob/8864b46849b031a3013764d03e167222963c0f5d/igraph/drawing/__init__.py
        - E substituir a função '_repr_svg_' pela '_repr_png_' do seguinte forum:
            https://stackoverflow.com/questions/30640489/issue-plotting-vertex-labels-using-igraph-in-ipython
"""

from igraph import Graph
from igraph import plot #visualização dos grafos

"""
    Parâmetros:
        - edges: arestas ([(0,1), (1,2), (2,3), (3,0)]), ou seja, 0 está conectado
        ao 1, 1 está conectado ao 2, 2 está conectado ao 3 e 3 está conectado ao
        0.
        - directed: indica se é ou não direcionado 
        
        Obs: pelas nossas configurações no edges, há um caminho do nó 0 para o
        nó 1, mas não há um caminho do nó 1 para o nó 0, porque ele é direcionado
"""

#EXEMPLO 1

grafo1 = Graph(edges = [(0,1), (1,2), (2,3), (3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount()) # para colocar as labels em cada vertice

print(grafo1)

plot(grafo1, bbox = (300, 300))

#EXEMPLO 2

grafo2 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (0,3), (3,2), (2,1), (1,0)], directed = True)
grafo2.vs['label'] = range(grafo2.vcount()) # para colocar as labels em cada vertice
plot(grafo2, bbox = (300, 300))

#EXEMPLO 3 (auto direcionamento)

grafo3 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (1,1)], directed = True)
grafo3.vs['label'] = range(grafo3.vcount()) # para colocar as labels em cada vertice
plot(grafo3, bbox = (300, 300))

#EXEMPLO 4 (vertice 5 foi add e não conectado (grafo disconexo))

grafo4 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (1,1)], directed = True)
grafo4.add_vertex(5)
grafo4.vs['label'] = range(grafo4.vcount()) # para colocar as labels em cada vertice
plot(grafo4, bbox = (300, 300))







