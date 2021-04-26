# -*- coding: utf-8 -*-

# 2 - Loops y funciones





a = 1

while a < 21 : # La sentencia "while" ejecuta los comandos mientras la condición tenga el valor True
    print(a) # Los comandos encadenacos a la sentencia deben tener sangría de 4 espacios
    a = a + 1 # Y debemos estar seguros que la condición en algún momento pase a False.

a = 1

while a-21 : # Enteros distintos a 0 son leídos como True, mientras que 0 es leído como False
    print(a)
    a = a + 1





b = input("¿Cuántos años tienes?: ") # input() permite que el usuario ingrese un valor a través de la consola

b # El resultado ingresado se almacena como cadena de texto

b = int(input("¿Cuántos años tienes?: ")) # Para lo siguiente, necesitamos que el resultado se ingrese como entero

if b >= 18 : # La sentencia "if"  ejecuta las condiciones encadenadas si la condición toma el valor True
    print("Usted es adulto")

if b >= 18 :
    print("Usted es adulto")
elif b < 18 : # Si la condición de "if" toma el valor False, Python saltará los comandos encadenados hasta el próximo "elif", y ejecutará los comandos encadenados si la condición toma el valor True
    print("Usted no es adulto")
    
if b >= 18 :
    print("Usted es adulto")
elif b >= 7 :
    print("Usted no es adulto")
elif b >= 0 :
    print("¡Usted solo es un niño! ¡Vaya a jugar con sus amigos!")
else : # La sentencia "else" es un complemento de "if" y ejecutará los comandos encadenados solo si ninguna condición señalada en "if" y "elif" toma el valor True
    print("Usted ingreso una edad negativa")





c = ["Demanda", "Oferta", "Equilibrio", "Utilidad"]

for aux in c : # La sentencia "for" ejecutará los comandos encadenados, definiendo una variable (en este caso "aux") que tomará los valores de la lista "c"
    print(aux, " contiene ", aux.count("a"), " veces la letra \"a\"")





d = range(4,15) # La función range() crea una lista de enteros

d # Nótese que no se puede ver así

type(d) # Es de tipo rango

list(d) # Es necesario transformarlo a tipo lista para ver que contiene. No contiene el límite superior

list(range(10)) # Podemos especificar solo el límite superior

list(range(0,15,3)) # Podemmos ajustar los pasos con un tercer input

e = []

for d in range(0,15) : # range() es útil para los loops
    if d % 2 == 0 :
        print(d, " es un número iar")
        e = e + ["Par"]
    else:
        print(d, " es un número impar")
        e = e + ["Impar"]

print(e)





import math # python trae consigo una serie de módulo que incluyen funciones muy útiles. Por ejemplo, el módulo "math" trae varias facilidades matemáticas



for f in range(1,10000) : 
    g = (1+1/f)**f
    print("La función evaluada en", f, "tiene valor de ", g)
    if abs(g-math.exp(1))<math.exp(-7):
        break # "break" termina el "for" o "while" más cercano

for f in "Caoanasauamao" :
    if f == "a" :
        continue # "continue" salta a la siguiente iteración del "for" o "while" más cercano
    print(f)

for f in range(1,10000) :
    pass # "pass" no hace nada





def odd_list(n) : # podemos definir una función con "def", seugido del nombre y sus inputs entre paréntesis
    """Aquí se puede agregar la documentación de la función"""
    for h in range(1,n+1) : # los comandos asociados deben ir con sangría
        if h % 2 != 0 :
            print(h)
            
type(odd_list)
            
i = odd_list(345)

print(i) # En este caso, la función entrega el valor "None", pues no se ha especificado un output para la función

def odd_list(n) :
    odd_numbers = []
    for h in range(1,n+1) : # los comandos asociados deben ir con sangría
        if h % 2 != 0 :
            odd_numbers = odd_numbers.append[h]
    return odd_numbers

i = odd_list(345)

print(i)





def story(ch_name, age, pet_name, pet="perro", lugar="plaza", accion="jugar") : # Nótese la distinción de argumentos que no tienen un valor default, y aquellos que sí los tienen. Estos últimos deben ser listados al final.
    print("Esta es la historia de", ch_name, ", el cual tiene", age, "años, y su", pet, "llamado", pet_name, ", los cuales iban a la", lugar, "para", accion)
    
story("Martín", 25 , "Max") # Los argumentos con valor por default se pueden omitir al llamar la función.

story("Martín", 25 , "Max", "gato", "parque") # Sin usar palabras claves, podemos añadir argumentos de forma posicional (en orden)

story("Martín", 25 , "Max", accion="cantar", lugar="biblioteca") # Podemos usar la palabra clave para saltar argumentos que dejaremos en default (no importa el orden)

story("Martín", 25 , "Max", "gato", lugar="playa") # Podemos usar tanto posicionales como por palabra clave, aunque estos últimos deben ir después

story("Martín", 25 , "Max", pet="gato", "parque") # Esto arrojará error

story(lugar="playa", ch_name="Mario", age=78, pet_name="Luigi", accion="Bailar") # Los argumentos sin valor por default también pueden ser llamados por palabra clave





def j(x, L=[]): # Valores por omisión se evalúa solo la primera vez en el caso de algunos objetos mutables como listas. Esto se aprecia en el siguiente ejemplo.
    L.append(x)
    return L

print(j(1))
print(j(2))
print(j(3))

def j(x, L=None): # Esto soluciona el problema
    if L is None:
        L = []
    L.append(x)
    return L

print(j(1))
print(j(2))
print(j(3))





def description(name, *descripcion, **datos_extra) : # Se pueden agregar argumentos de cantidad arbitraria, usando "*"y "**". Estos deben ir al final de los argumentos regulares. Aquellos asociados a "*" son ingresados como lista, y aquellos asociados a "**" son ingresados como diccionario
    print(name, "es una persona muy:")
    for k in descripcion :
        print("-", k)
    print("Además, acá van algunos datos extra de", name, ":")
    datos = datos_extra.keys()
    for k in datos :
        print(k,"-->", datos_extra[k])

#                     |-------------- *descripcion -----------------|  |------------------------------- **datos_extra -----------------------------|
description("Martín", "Inteligente", "Guapa", "Simpática", "Generosa", Nacimiento="10 de Enero de 1995", Signo="Capricornio", Edad=25, Sexo="Hombre")

l = [0,21,2]

list(range(*l)) # Podemos hacer el proceso inverso: desempaquetar una lista como argumentos de una función usando "*". También podemos hacer lo mismo con un diccionario y el indicador "**" de forma análoga





# Hasta ahora he escrito los código según me plazca, pero existen ciertas convenciones a la hora de escribir códigos en Python.
# Es importante en algún momento leer la guía de Python Enhancement Proposals (PEP) 8 : https://www.python.org/dev/peps/pep-0008/