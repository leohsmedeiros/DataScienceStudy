# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
from keras.models import Sequential
#camada densa (significa que todos os neuronios da camada de entrada estão conectados com todos os neurônios da camada oculta, e cada neurônio da camada oculta está conectado ao próximo neurônio da camada oculta)
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix

"""
    Vamos fazer a implementação da rede neural utilizando a base de dado Iris e
    vamos utilizar a biblioteca keras (que roda em cima do tensorflow (framework
    para trabalhar com Deep Learning, desenvolvido pela Google)), que é uma
    das mais utilizadas em python para trabalharmos com Deep Learning
"""

base = datasets.load_iris()
#em previsores temos os 4 atributos da base de dados iris
previsores = base.data
#em classe temos as respectivas respostas
classe = base.target

"""
    essa parte do codigo é necessária, pq temos 3 classes (0, 1 e 2),
    isso indica que a camada de saída terá 3 neurônios, um neurônio para cada
    uma das classes (isso é bem comum quando trabalhamos com problemas de 
    classificação, em que temos mais de dois valores)
    
    O y_teste e o y_treinamento estão com aqueles valores individuais e
    precisamos que eles estejam no formato da classe dummy, por isso vamos
    passar a classe_dummy para o train_test_split

"""

classe_dummy = np_utils.to_categorical(classe)

#desta forma vamos ter 105 registros para fazer o treinamento e 45 registros para os testes
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe_dummy,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

#inicializando uma rede neural que tem esse comportamento sequencial
modelo = Sequential()

"""
    como vimos nas aulas teóricas, a quantidade de neurônios na camada de entrada
    equivale a quantidade de atributos que temos como previsores (neste caso,
    temos 4 atributos previsores)
"""

#input_dim: quantos neurônios terá na sua camada de entrada
#temos 4 neurônios da camada de entrada que estarão vinculadas a 5 neurônios da primeira camada escondida
modelo.add(Dense(units = 5, input_dim = 4))
modelo.add(Dense(units = 4)) # vamos adicionar mais uma camada escondida
modelo.add(Dense(units = 3)) #camada de saída

modelo.summary()

#imprimir
from keras.utils.vis_utils import plot_model

#optimizer: algoritmo de ajuste dos pesos (adam é o mais utilizado)
#loss: algoritmo de calculo do erro
#metrics: que é como vc deseja visualizar os resultados
modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy')

#epochs: número de épocas que vc quer que rode o algoritmo (por padrão deixamos 1000)
#validation_data: vai fazer o treinamento e testar com a base de dados de teste
modelo.fit(X_treinamento, y_treinamento, epochs = 1000,
           validation_data = (X_teste, y_teste))

"""
    Predict vai retornar a probabilidade de cada linha (atributo), pertencer a
    um determinado grupo (coluna)
    
    No Spyder do Anaconda, ele coloca o atributo com maior probabilidade em
    cada linha
"""
previsoes = modelo.predict(X_teste)
previsoes = (previsoes > 0.5) #para colocar como true o atributo que tenha mais de 50% de chance de ser classificado com aquele respectivo grupo


#visualizer = ConfusionMatrix(modelo)
#ocasionaria erro, então vamos fazer de outro modo

#vai pegar os indices dos maiores valores
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsao_matrix = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matrix, y_previsao_matrix)


