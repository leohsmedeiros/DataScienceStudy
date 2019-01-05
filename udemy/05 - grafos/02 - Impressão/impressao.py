#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot

"""
    Veremos algumas técnicas para impressão e visualização do grafo
"""

grafo = Graph(edges = [(0,1), (2,3), (0,2), (0,3)], directed = True)
grafo.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo.vs['peso'] = [40, 30, 30, 25]
grafo.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo.es['weight'] = [1,2,1,3]

for v in grafo.vs:
    print(v)

for e in grafo.es:
    print(e)

#caso eu queira cores diferentes para cada vértice
grafo.vs['cor'] = ['blue', 'red', 'yellow', 'green']

plot(grafo, bbox = (300, 300),
     vertex_size = grafo.vs['peso'], #vertex_size vai ajustar o tamanho de cada nó, de acordo com o atributo passado como parâmetro
     edge_width = grafo.es['weight'], #edge_width vai ajustar a largura de cada aresta, de acordo com o atributo passado como parâmetro
     vertex_color = grafo.vs['cor'], #vertex_color vai alterar a cor de cada nó, de acordo com o atributo passado como parâmetro
     edge_curved = 0.4, #vai criar uma curva entra as arestas
     vertex_shape = 'square') #vai trocar o shape de esfera de cada nó, por quadrado














