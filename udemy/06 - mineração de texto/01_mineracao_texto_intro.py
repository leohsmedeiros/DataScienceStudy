#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import nltk #natural language toolkit

#vai abrir uma janela, onde pode fazer o download de todos os pacotes
#nltk.download()

from nltk.corpus import PlaintextCorpusReader

corpus = PlaintextCorpusReader('Arquivos', '.*') #.*: todas as extensões

arquivos = corpus.fileids()
arquivos[0]
arquivos[0:100]
for a in arquivos:
    print(a)

texto = corpus.raw('1.txt') #conteúdo
todo_texto = corpus.raw() #todos os textos em todos os arquivos
palavras = corpus.words() #não mostra no variable explorer e mostra apenas '...' no console, pois é um vetor muito grande
palavras[1] #visualizar a segunda palavra
len(palavras) #contagem de palavras











