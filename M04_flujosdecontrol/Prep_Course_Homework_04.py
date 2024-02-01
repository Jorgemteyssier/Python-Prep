#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
x=8
if x>=0:
    print(x)




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
y=8
z=19
if type(y)==type(z):
    print('las variables son el mismo tipo de dato')
else:
    print('las variables son distintos tipos de datos')




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for a in range(1,21):
    if a%2 == 0:
        print(a,'es par')
    else:
        print(a,'es impar')





# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for t in range (0,6):
    print(t,'elevado a la 3 es',t**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
q=7
for s in range (0,q):
    print(s)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
j=10
if type(j)==int:
    if j>0:
        factorial=j
        while j>2:
            j=j-1
            factorial=factorial*j
        print(factorial)
    else:
        print('es menor a 0')
else:
    print('no es entero')






# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
z=5
while z>0:
    for m in range(1,z):
        if m%2==0:
            print(m)
    z=z-1
    




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
for k in range(2,6):
    if k>=5:
        print('la variable es mayor o igual a 5')
    else:
        while k<5:
            print(k)
            k=k+1




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
valormax=2000
valormin=0
primo=True
while valormin<=valormax:
    if valormin>1:
        for division in range (2,valormin):
            resto=valormin%division
            if(resto==0):
                primo=False
        if (primo):
            print(valormin)
        else:
            primo=True
    valormin+=1



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
valormax=2000
valormin=0
primo=True
while valormin<=valormax:
    if valormin>1:
        for division in range (2,valormin):
            resto=valormin%division
            if(resto==0):
                primo=False
                if primo==False:
                    break
        if (primo):
            print(valormin)
        else:
            primo=True
    valormin+=1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
#sí, los ciclos son menos ya que al encointrar el primer residuo = 0 ya no es necesario seguir haciendo las demás divisiones 
valormax=30
valormin=0
primo=True
ciclos_sin_break=0
while valormin<=valormax:
    if valormin>1:
        for division in range (2,valormin):
            ciclos_sin_break += 1
            resto=valormin%division
            if(resto==0):
                primo=False
        if (primo):
            print(valormin)
        else:
            primo=True
    valormin+=1
print(f'cantidad de ciclos sin break {ciclos_sin_break}')


valormax=30
valormin=0
primo=True
ciclos_con_break=0
while valormin<=valormax:
    if valormin>1:
        for division in range (2,valormin):
            ciclos_con_break += 1
            resto=valormin%division
            if(resto==0):
                primo=False
                if primo==False:
                    break
        if (primo):
            print(valormin)
        else:
            primo=True
    valormin+=1
print(f'cantidad de ciclos con break {ciclos_con_break}')



# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
xxxx=100
while xxxx<=300:
    xxxx+=1 
    if xxxx>=100:
        if xxxx%12 != 0:
            continue
        print(xxxx)  




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
respuesta=True
while respuesta:
    numero_primo=input('Escribe un número entero y positivo')
    if int(numero_primo)>0:
        valormin=int(numero_primo)
        primo=True
        if valormin>1:
            for division in range (2,valormin):
                if(valormin%division==0):
                    primo=False
                    if primo==False:
                        print(f'{valormin} no es primo')
                        break
                        
            if (primo):
                print(f'{valormin} sí es primo')

            else:
                primo=True
    else:
        print('el número no es positivo')
    conitnuar=input('Checar otro número responda si o no')
    if conitnuar== 'si':
        respuesta=True
    else:
        respuesta=False
        print('fin del programa')



#una forma donde te los va dando consecutivos pero no puedes checar el que tu quieras
        
busqueda=True
valormin=0
primo=True
while busqueda:
    if valormin>1:
        for division in range (2,valormin):
            resto=valormin%division
            if(resto==0):
                primo=False
                if primo==False:
                    break
        if (primo):
            print(f'El numero {valormin} es primo')
            seguir=input("buscar el siguiente numero primo 'si' o 'no'")
            if seguir=='no':
                print('fin de la busqueda')
                busqueda=False
                break

        else:
            primo=True
    valormin+=1



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

f=100
while f<=300:
    if f%6==0:
        print(f)
        break
    f+=1

