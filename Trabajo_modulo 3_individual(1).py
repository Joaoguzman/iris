#!/usr/bin/env python
# coding: utf-8

# Se desarrolla el ejercicio primero en pandas y luego como un conjunto de listas.

# In[19]:


import pandas as pd
import csv
import statistics
from tabulate import tabulate
import urllib


# In[20]:


#PUNTO 2 Y 3
import csv
with open('data/iris.data', 'r') as file:
    reader = csv.reader(file)
    for linea in reader:
        print(linea)
    datos = list(reader)


# In[21]:


with open('data/iris.data', "r") as archivo:
    data = csv.reader(archivo)
    header = ['largo_sepalo', 'ancho_sepalo', 'largo_petalo', "ancho_petalo", "especie"]
    df = pd.DataFrame(data, columns=header)
    print(df.head())
    print(df.info())
    


# In[22]:


df[["largo_sepalo", "ancho_sepalo", "largo_petalo", "ancho_petalo"]].describe()


# In[23]:


columnas = df.columns.drop('especie')
df[columnas] = df[columnas].apply(pd.to_numeric, errors='coerce')


# In[24]:


df.describe()


# In[25]:


#PUNTO 5: se imprime el promedio de las cuatro primeras columnas
df.mean()


# In[26]:


df.describe()


# In[27]:


df.groupby(['especie']).mean()


# In[28]:


#PUNTO 6: Hay 50 casos por cada especie.
df.groupby(['especie']).count()


# In[29]:


#PUNTO 6: en total hay 150 casos
df["especie"].count()


# In[30]:


import csv
with open('data/iris.data', 'r') as file:
    reader = csv.reader(file)
    lista=[['largo_sepalo', 'ancho_sepalo', 'largo_petalo', "ancho_petalo", "especie"]]
    for linea in reader:
        lista.append(linea)

#fieldnames = ['largo_sepalo', 'ancho_sepalo', 'largo_petalo', "ancho_petalo", "especie"]
print(len(lista))


# In[31]:


print(tabulate(lista))


# In[32]:


print(len(lista))
lista.pop(-1)
len(lista)


# In[33]:


#PUNTO 5: VERSION CON LISTAS.

def promedio(especie, variable, lista):
    variables = ['largo_sepalo', 'ancho_sepalo', 'largo_petalo', "ancho_petalo", "especie"]
    indice_variable = variables.index(variable)
    acumulador= 0
    contador = 0
    for elemento in lista:
        if elemento[4] == especie:
            contador = contador + 1
            acumulador = acumulador + float(elemento[indice_variable])
    return round(acumulador/contador, 2)
especies = ["Iris-versicolor", "Iris-setosa", "Iris-virginica"]
variables = ['largo_sepalo', 'ancho_sepalo', 'largo_petalo', "ancho_petalo", "especie"]
for especie in especies:
    print("El promedio de " 
      + variables[0] 
      + " de las especies "
      + especie 
      + " es: ", 
          promedio(especie, variables[0], lista))
for especie in especies:
    print("El promedio de " 
      + variables[1] 
      + " de las especies "
      + especie 
      + " es: ", 
          promedio(especie, variables[1], lista))
for especie in especies:
    print("El promedio de " 
      + variables[2] 
      + " de las especies "
      + especie 
      + " es: ", 
          promedio(especie, variables[2], lista))
for especie in especies:
    print("El promedio de " 
      + variables[3] 
      + " de las especies "
      + especie 
      + " es: ", 
          promedio(especie, variables[3], lista))




# In[34]:


#PUNTO 7: 
#Modifique los datos de las filas número 1, 10, 30 y 100, 
#asignando elvalor 0 a cada uno de los valores de las primeras 4 columnas. 
#Asigne elvalor N/A al valor de la columna ‘especie’ en esas primeras filas.
for indice in range(0,101):
    
    if indice == 1 or indice == 10 or indice == 30 or indice == 100:
        lista[indice] = [0, 0, 0, 0, "N/A"]


# In[35]:


print(lista[1], lista[10], lista[30], lista[100])


# In[36]:


#Punto 8:
len(lista)


# In[37]:


#Guardar archivo
with open("iris_editado.csv", "w") as f:
  writer = csv.writer(f)
  writer.writerows(zip(lista))


# In[38]:


csv = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(csv)                                                                                                


# In[ ]:




