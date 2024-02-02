#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
lista_vacia=[]
x=-1
while x>-16:
    lista_vacia.append(x)
    x-=1

lista_vacia.sort()
print(lista_vacia)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

#Sí
y=0
while y < len(lista_vacia):
    elemento=lista_vacia[y]
    if elemento%2 == 0:
        print(elemento)
    y+=1



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for z in lista_vacia:
    if z%2 ==0:
        print(z)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

b=iter(lista_vacia)
print(next(b))
print(next(b))
print(next(b))

for t in lista_vacia[:3]:
    print(t)
# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for w in enumerate(lista_vacia):
    print(w)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista_1=[1,2,5,7,8,10,13,14,15,17,20]
for p in range(1,21):
    s=p in lista_1
    if s == False:
     lista_1.append(p)
lista_1.sort()
print(lista_1)



# In[11]:


#Este es el que estaba en el resuelto otra forma de hacerlo ver que aquí ingresa el numero faltante en el indice con insert, esto puede servir en listas en donde el orden sea distinto a el orden numerico o alfabetico
lista = [1,2,5,7,8,10,13,14,15,17,20]
n = 1  # Inicializa la variable n con el valor 1

while n <= 20:  # Mientras n sea menor o igual a 20, se ejecuta el bucle
    if not (n in lista):  # Verifica si n no está presente en la lista
        lista.insert(n-1, n)  # Inserta el valor de n en la posición (n-1) de la lista
    n += 1  # Incrementa el valor de n en 1 en cada iteración

print(lista)  # Imprime la lista resultante



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

lista_fibo=[0,1]
while len(lista_fibo)<30:
    x=len(lista_fibo)
    n1=lista_fibo[x-1]
    n2=lista_fibo[x-2]
    numero_fibo=n1+n2
    lista_fibo.append(numero_fibo)
print(lista_fibo)
#codigo de la tarea ya resuelta 
#muy similar las diferencias son que se usa una variuable dada en vez de la longitu de la lista con lo cual se tienbe que ir aumentando la variable y yo dentro del coclo while designe varias variables para hacerlo mas comprensivo a mi parecer ambas formas son buenas
fibo = [0, 1]  # Crea una lista inicial con los primeros dos números de la secuencia de Fibonacci

n = 2  # Inicializa la variable n con el valor 2

while n < 30:  # Mientras n sea menor que 30, se ejecuta el bucle
    fibo.append(fibo[n - 1] + fibo[n - 2])  # Agrega el siguiente número de Fibonacci a la lista
    n += 1  # Incrementa el valor de n en 1 en cada iteración

print(fibo)  # Imprime la lista de la secuencia de Fibonacci


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:




# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:




# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:





# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:





# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:





# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:





# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:





# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:




# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:



