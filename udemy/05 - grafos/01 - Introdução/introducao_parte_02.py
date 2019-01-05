#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot

grafo1 = Graph(edges = [(0, 1),(2,2), (2,3), (3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)

"""
    Resultado:
        IGRAPH D--- 4 4 --
        + attr: label (v)
        + edges:
        0->1 2->2 2->3 3->0
        
        
    Analisando "D--- 4 4 --"
        - Primeiro parâmetro (D): direcionado, se fosse não direcionado seria U
        - Segundo parâmetro: nome do grafo
        - Terceiro parâmetro: colocaria um W se fosse um grafo ponderado (com peso)
        - Quarto e quinto parâmetros (4 4): indica quantos vértices e quantas
        arestas nós temos, respectivamente
        
    Analisando "0->1 2->2 2->3 3->0"
        - as flechas indicam q ele é direcionado, e pra qual direção cada vértice
        está indo        
"""

grafo2 = Graph(edges = [(0, 1),(2,2), (2,3), (3,0)], directed = False)
print(grafo2)

"""
    Resultado:
        IGRAPH U--- 4 4 --
        + edges:
        0--1 2--2 2--3 0--3
        
    Desta vez apareceu U ao invés de D, pois o grafo 2 não é direcionado, e
    apenas - ao invés das setas.
"""
grafo3 = Graph(directed = False)
grafo3.add_vertices(10) #add 10 vertices
grafo3.add_vertex(16) #add 1 vertice com indice 16
grafo3.add_edges([(0,1), (2,2), (2,3), (3,0)])
print(grafo3)
plot(grafo3, bbox = (300,300))


grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1), (1,2), (2,3), (3,4), (4,0)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plot(grafo4, bbox = (300,300))



