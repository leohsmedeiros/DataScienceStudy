#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist


(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()

X_treinamento = X_treinamento.reshape(len(X_treinamento), np.prod(X_treinamento.shape[1:]))
X_teste = X_teste.reshape(len(X_teste), np.prod(X_teste.shape[1:]))

X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

X_treinamento /= 255 #255 valor maximo do intervalo dos bytes RGB
X_teste /= 255 #255 valor maximo do intervalo dos bytes RGB

y_treinamento = np_utils.to_categorical(y_treinamento, 10) #10 números de classes (que variam de 0 até 9)
y_teste = np_utils.to_categorical(y_teste, 10)

"""
    Agora que temos estes dados pré-processados, vamos dar início a nossa rede
    neural
"""

#usamos esta classe pois estamos trabalhando com uma sequencia de camadas
modelo = Sequential()


"""
    Parametros:
        - activation: vamos passar 'relu', pois é uma das funções mais utilizadas
        em DeepLearning e tem tido bons resultados ao trabalhar com processamento
        de imagens.
        basicamente, quando ela recebe um valor que seja maior do que 1, ela
        vai retornar o proprio valor, se for negativo, retorna 0
        - input_dim: quantidade de neurônios na entrada. Neste caso, 784,
        lembrando que o número de neurônios que eu tenho na camada de entrada
        equivale ao número de características que temos na base de dados
"""

modelo.add(Dense(units = 64, activation = 'relu', input_dim = 784))

#quando temos muitas entradas, a camada de Dropout vai servir para que nós zeremos algumas entradas
#vai evitar o overfitting, que é se adaptar a uma base de dados e apresentar performance baixa em uma base nova
modelo.add(Dropout(0.2)) #ou seja, desses 64 neurônios, ele vai zerar 20% desses neurônios, enquanto estiver fazendo o treinamento

modelo.add(Dense(units = 64, activation = 'relu', input_dim = 784))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))

#camada saida
#softmax vai passar a probabilidade de ser cada letra
modelo.add(Dense(units = 14))

modelo.summary()

modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
historico = modelo.fit(X_treinamento, y_treinamento, epochs = 20, validation_data = (X_teste, y_teste))

historico.history.key()
plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_acc'])

previsoes = modelo.predict(X_teste)
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsoes_matrix = [np.argmax(t) for t in previsoes]
confusao = confusion_matrix(y_teste_matriz, y_previsoes_matriz)

novo = X_treinamento[20]
novo = np.expand_dims(novo, axis = 0)
pred = modelo.predict(novo)