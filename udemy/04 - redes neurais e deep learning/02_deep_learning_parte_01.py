#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist

#vai carregar uma base de dados em imagens (no formato RGB)
(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()

#para mostrar a imagem
plt.imshow(X_treinamento[0])

#para mostrar a imagem em escala de cinza
plt.imshow(X_treinamento[0], cmap = 'gray')

#visualizar a classe
plt.title(y_treinamento[0])

#vai agrupar os pixels de cada imagem (esse formato é necessário para a biblioteca)
#são 60 mil imagens, para 784 bytes
X_treinamento = X_treinamento.reshape(len(X_treinamento), np.prod(X_treinamento.shape[1:]))
X_teste = X_teste.reshape(len(X_teste), np.prod(X_teste.shape[1:]))

#precisamos converter de int para float32 pq é necessario fazermos uma normalização desses valores
#é necessário tbm para fazermos o processamento de forma mais rápido
X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

X_treinamento /= 255 #255 valor maximo do intervalo dos bytes RGB
X_teste /= 255 #255 valor maximo do intervalo dos bytes RGB


y_treinamento = np_utils.to_categorical(y_treinamento, 10) #10 números de classes (que variam de 0 até 9)
y_teste = np_utils.to_categorical(y_teste, 10)







