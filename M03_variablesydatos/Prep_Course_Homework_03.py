#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
x=5



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
pirnt(type(x))




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre='Jorge Miranda'



# 5) Crear una variable que contenga un número complejo

# In[3]:
z=5+6j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(z))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
a=True
b='True'
#son diferentes uno es un valor bool y otro un str



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(a))
print(type(b))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
r=5+3.5




# 11) Realizar una operación de suma de números complejos

# In[2]:

y+(5+3j)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

5+y



# 13) Realizar una operación de multiplicación

# In[5]:

pi*x



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

k=27/4
print(k)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print(int(k))
27//4



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

27%4



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

6*4+3



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

d='hola '
f='mundo'
d+f



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

'2'==2 #uno es string y el otro es entero por eso es falso



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int('2')==2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#por que lleva punto en vez de coma



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

p=3
p-=1
print(p)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2 #con la operacion << recorres el numero de lugares que indica el valor de la derecha al valor de la izquierda hacia la izquierda completando el número con ceros esto dentro del sistema binario en sistema binario 1=1 al aplicar la operación se convierte en 100 que es igual a 4, esto por que etsamos trabajando en base binaria o base 2 en un cambio de bases de decimal a 2 dentro de la operación 



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


#no puedes sumar un str con un int por eso no sé permite, y las operaciones darían 4 si se transformaran los dos valores a int o 22 si se transforman los dos datos a str 



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
'hola '*3


