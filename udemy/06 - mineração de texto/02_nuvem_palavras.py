#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords #palavras que não tem muito significado num contexto
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud

"""
    Vamos fazer a geração de uma nuvem de palavras, para verificarmos quais
    palavras aparecem mais
"""


corpus = PlaintextCorpusReader('Arquivos', '.*')

arquivos = corpus.fileids()
texto = corpus.raw('1.txt')

todo_texto = corpus.raw()
palavras = corpus.words()

#stopwords.words('portuguese'): palavras em português
#Neste exemplo vamos trabalhar com textos em inglês
stops = stopwords.words('english') #vamos remover essas palavras do nosso texto
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])
nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 100)

nuvem.generate(todo_texto)
plt.imshow(nuvem)
