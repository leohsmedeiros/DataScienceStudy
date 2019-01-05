#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from igraph import Graph
from igraph import plot


grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1), (1,2), (2,3), (3,4), (4,0)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)

grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #mudará apenas a label dos vértices do grafo (na visualização)
grafo4.vs['name'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #mudará o identificador de cada vértice

#matriz de adjacência
print(grafo4.get_adjacency()) 
grafo4.get_adjacency()[0,] #vai pegar da linha 0, todas as colunas

#para visualizar o nome dos vértices
for v in grafo4.vs: #retorna todos os vértices
    print(v)

plot(grafo4, bbox = (300,300))



grafo5 = Graph(edges = [(0,1), (2,3), (0,2), (0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']

#é preciso passar a mesma quantidade de acordo com o número de vértices
grafo5.vs['peso'] = [40, 30, 30, 25]

#for para percorrer os vértices
for v in grafo5.vs:
    print(v)
grafo5.vs[0] #para visualizar o vértice de indice 0

#for para percorrer as arestas
for e in grafo5.es: #es de edges
    print(e)
grafo5.es[0] #para visualizar a aresta de indice 0
    
grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo'] #TipoAmizade é uma propriedade criada (se não existir como padrão, ele cria como nova)
grafo5.es['TipoAmizade'] #para visualizar os tipos de amizade

"""
    Adicionando pesos
"""
grafo5.es['weight'] = [1,2,1,3]  #weight é uma propriedade já do igraph  (se não existir como padrão, ele cria como nova)

print(grafo5)

grafo5.vs['type'] = 'Humanos'
grafo5['name'] = 'Amizades'
plot(grafo5, bbox = (300,300))

