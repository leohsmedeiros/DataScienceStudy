#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import string

"""
    Vamos analisar quais são os termos mais frequêntes
"""

corpus = PlaintextCorpusReader('Arquivos', '.*')

arquivos = corpus.fileids()
texto = corpus.raw('1.txt')

todo_texto = corpus.raw()
palavras = corpus.words()

stops = stopwords.words('english')
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])
nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 100)

nuvem.generate(todo_texto)
plt.imshow(nuvem)

"""
    Tirando as stop words (palavras que não fazem sentido isoladas):

    estamos percorrendo cada uma das palavras que está na variável palavras,
    porém vamos colocar dentro dessa nova lista 'palavras_sem_stop_words', 
    somente aquelas que não estão na lista 'stops'.
    
    Perceba que houve uma redução significativa no conjunto de palavras restantes.
"""
palavras_sem_stop_words = [p for p in palavras if p not in stops]
len(palavras_sem_stop_words)

#agora vamos retirar pontuações (que não estão presentes no stop words)
string.punctuation

palavras_sem_pontuacao = [p for p in palavras_sem_stop_words if p not in string.punctuation]
len(palavras_sem_pontuacao)

#em value aparece a frequencia de quantas vezes a key aparece
frequencia = nltk.FreqDist(palavras_sem_pontuacao)
palavras_mais_comuns = frequencia.most_common(100)
























