#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
ciudades=['México','Buenos Aires','Lima','Bogotá','Madrid','Caracas']

type(ciudades)

print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print(ciudades[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print(ciudades[1:4])




# 4) Visualizar el tipo de dato de la lista

# In[12]:

type(ciudades)



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(ciudades[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print(ciudades[:4])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

#no va a arrojar error ya que las listas si aceptan duplicados. Los sets son los que no ni los diccionarios en las claves 
ciudades.append('Monterrey')
ciudades.append('Madrid')
print(ciudades)







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

ciudades.insert(3,'Cancún')

print(ciudades)

# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
ciudades_angloparlantes=['Miami','Londres','Sídney',]
ciudades.extend(ciudades_angloparlantes)
print(ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

ciudades.index('Madrid')
#Te da el indice de el primero que encuentra



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

#Da error 
# ciudades.index('Milan')
# ValueError: 'Milan' is not in list



# 12) Eliminar un elemento de la lista

# In[25]:

ciudades.remove('Madrid')

print(ciudades)
#Nota: al igual que en el indice, si hay dos elementos repetidos y eliminas uno elimina el primero en encontrar

# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
#Da error
#ciudades.remove('Mónaco')
#ValueError: list.remove(x): x not in list




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
ultimo_elemento=ciudades.pop()
print(ciudades)
print(ultimo_elemento)



# 15) Mostrar la lista multiplicada por 4

# In[29]:
ciudades*4




# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
tupla_1=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(tupla_1)
type(tupla_1)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(tupla_1[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
20 in tupla_1
30 in tupla_1
print(20 in tupla_1)
print(30 in tupla_1)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

x='Paris'
if(not(x in ciudades)):
    ciudades.append(x)
    print('se agrego el elemento')
else:
    print('el elemento ya estaba')

print(ciudades)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(ciudades.count('México'))
print(tupla_1.count(20))



# 21) Convertir la tupla en una lista

# In[52]:

b=list(tupla_1)
type(b)
print(b)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
var1,var2,var3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_=tupla_1
print(var1)
print(var2)
print(var3)



# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
dic1={'Ciudad':ciudades,'País':['México','Argentina','España','Perú','Venezuela','Colombia','Inglaterra','Estados Unidos','Australia','Francia'],'Continente':['América','Europa','Oceanía']}





# 24) Imprimir las claves del diccionario

# In[59]:
dic1.keys()



# 25) Imprimir las ciudades a través de su clave

# In[61]:

dic1['Ciudad']
print(dic1['Ciudad'])

