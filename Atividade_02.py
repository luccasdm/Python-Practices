#!/usr/bin/env python
# coding: utf-8

# <h1>LISTA DE EXERCÍCIOS</h1>

# In[6]:


import math
import numpy as np


# <b><p>Exercícios 01 - Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,&#39;hum&#39;, &#39;dois&#39;]. A ideia do exercício é
# tirar a média de todos os valores contidos na lista, porém para fazer o cálculo
# precisa remover as strings.</p></b>

# In[30]:


lista = [6,7,4,7,8,4,2,5,7,'hum', 'dois']

media = sum(lista[0:9]) / len(lista)

print('A média é da lista é = ', media)


# <b><p>Exercício 02 - Crie um método que receba duas matrizes, some os valores total de cada matriz e
# depois multiple o resultado delas e retorne o valor.</p></b>

# In[33]:


matriz_1 = np.array([[2,2], 
                     [4,1], 
                     [6,4]])

matriz_2 = np.array([[2,4], 
                     [1,64], 
                     [3,4]])


def recebe_matriz(mat1, mat2):

    soma_matriz_1 = mat1.sum()

    soma_matriz_2 = mat2.sum()

    mult = soma_matriz_1 * soma_matriz_2
                                  
    print('O resultado da multiplicação da Matriz 1 com a Matriz 2 é: ', mult)

recebe_matriz(matriz_1, matriz_2)


# <b><p>Exercício 03 - Criar uma matriz nxm (n = 5, m =7)<br>
# a. faça a matriz transposta desta matriz</p></b>

# In[43]:


matriz_exs_03 = np.random.rand(5,7)
print('Matriz (5,7):\n', matriz_exs_03)

matriz_transposta = matriz_exs_03.T
print('Matriz Transposta:\n', matriz_transposta)


# <b><p>b. somar toda matrix</p>

# In[44]:


soma_total_matriz = matriz_exs_03.sum()
print('Soma total da Matriz: ', soma_total_matriz)


# <b>
#     <p>c. somar todas as colunas</p>

# In[46]:


soma_colunas_matriz = matriz_exs_03.sum(axis = 0)
print('Soma das colunas:\n', soma_colunas_matriz)


# <b>
#     <p>d. somar todas as linhas.</p>

# In[47]:


soma_linhas_matriz = matriz_exs_03.sum(axis = 1)
print('Soma das linhas:\n', soma_linhas_matriz)


# <b><p>e. retorne o maior valor</p>

# In[50]:


maior_valor = matriz_exs_03.max()
print('Maior valor da matriz: ', maior_valor)


# <b><p>f. retorne o menor valor.</p>

# In[51]:


menor_valor = matriz_exs_03.min()
print('Menos valor da matriz: ', menor_valor)


# <b><p>Exercício 04 - Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.</p></b>

# In[76]:


matriz_exs_04 = np.random.rand(5)

soma = sum(matriz_exs_03) + sum(matriz_exs_04)

print('Soma das Matrizes:\n', soma)


# <b><p>Exercício 05 - Crie um array de números que vai de 0 a.</p></b>

# In[80]:


array_random = np.arange(0,1001)
print(array_random)


# <b><p>Exercício 06 - Crie uma matriz só de zeros.</p></b>

# In[87]:


matriz_zero = np.zeros((2,2))
print(matriz_zero)

