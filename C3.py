# -*- coding: utf-8 -*-

# 3 - Datos tipo secuencia





A = ["a", "b", "c"] # Se mostrarán algunos métodos de lista

A.append("d") # Agrega un item

A

A.extend(["e", "f"]) # Agrega los elementos de una lista

A

A.insert(2, "x") # Agrega un item en posición dada

A

A.remove("x") # Remueve un item dado

A

A.pop(3) # Muestra el item de la posición dada, y lo elimina. Si no se especifica posición, se toma el último ítem

A

A.reverse() # Invierte la lista

A

A.sort() # Ordena la lista

A

A.index("c") # Devuelve la posición del item

A.count("c") # Devuelve la cantidad de veces que aparece el item





def f(x) : return type(x) == str

b = filter(f, [3, False, 45, "cosa", 4.87, "Saludos"]) # "filter" toma una función y la aplica a los elementos de la secuencia señalada.

type(b) # Devuelve un tipo filtro

list(b) # Al transformarlo a lista, vemos que "filter" devuelve los objetos para los cuales la función devuelve True





def f(x) : return x*10

c = map(f, [3, 7, 10, 465, 2.3]) # "map" toma una función y la aplica a los elementos de la secuencia señalada.

type(c) # Devuelve un tipo map

list(c) # Al transformarlo a lista, vemos que "map" devuelve los resultados de la función

def f(x,y) : return x*y

c = map(f, [3, 7, 10, 465, 2.3], [0, 1, 1, 0, 1]) # Se pueden usar funciones con más de un input. Es necesario entonces agregar tantas secuencias como argumentos se requieran

list(c)





from functools import reduce

def f(x,y) : return x+y

d = reduce(f, range(1,6)) # "reduce" aplica la función a los dos primeros elementos de la secuencia. El resultado, es aplicado con el tercero, así sucesivamente, obteniendo un único valor

d





e = [12, 43, 2, 3, 104]

f = [2, 4, 5, 1, 0]

[2*x for x in e] # Podemos crear nuevas listas a partir de otras de forma más intuitiva mediante listas de compresión

[2*x for x in e if x < 20]

[[x, x*2, x*3] for x in e]

[(x, x*2, x*3) for x in e]

[x+y for x in e for y in f]

[e[i]+f[i] for i in range(len(e))]





g = "Saludos", 3.4, 2+5j # Al no incluir corchetes en una secuencia estamos creando una dupla

g

type(g)

g = ("Saludos", 3.4, 2+5j) # Podemos hacero con paréntesis

g

h = 1, 2, g, 3 # Podemos anidar tuplas, y estas son inmutables (podemos hacer seccionado y concanetación para simular)

h

h = h[0], h[1], h[3]

h





i = () # Para crear una tupla vacía

i

i = "a", # Para crear un singleton

i

k, l, m = h # Para desempaquetar tuplas (y cualquier otra secuencia)

print(k)
print(l)
print(m)





n = ["Queso", "Masa", "Queso", "Salsa de tomate", "Queso", "Masa", "Pepperoni", "Pepperoni", "Queso"]

o = set(n) # Con la función "set" podemos crear objetos del tipo conjunto. Estos son grupos no ordenados y no repetidos de elementos

o

type(o)

"Queso" in o

"Piña" in o

p = {"Masa", "Queso", "Pino", "Queso"} # Podemos crear conjuntos con "{"

p # Nótese que al crear el conjunto, automáticamente se eliminan repeticiones

o - p # Elementos en "o" pero no en "p"

o | p # Elementos en "o" o en "p"

o & p # Elementos en "o" y en "p"

o ^ p # Elementos en "o" o en "p" pero no en ambos





q = {"Martín" : 2030, "Nicolás" : 123, "José" : 453, "Patricio" : 1000, "Vicente" : 1560} # Este es un objeto tipo diccionario. Estos son conjuntos de valores indexados por claves, de la forma "clave : valor"

q

type(q)

type({}) # Podemos crear diccionarios vacíos usando "{}"

q["Nicolás"]

q["Patricio"]

del q["José"] # Podemos eliminar objetos del diccionario usando "del"

q

q.keys() # Podemos obtener la lista de claves con el método "keys"

type(q.keys())

list(q.keys()) # Aunque hay que convertirlo en lista primero

dict([("Martín", 2030), ("Nicolás", 123), ("José", 453), ("Patricio", 1000), ("Vicente", 1560)]) # Podemos crear un diccionario ingresando una lista de duplas con la función "dict"

dict(Martín = 2030, Nicolás = 123, José = 453, Patricio = 1000, Vicente = 1560) # O de esta forma si las claves son cadenas





for r, s in q.items() : # Con el método "items" podemos iterar sobre un diccionario obteniendo tanto su clave como su valor
    print("Su nombre es", r, "y tiene un CI de", s)
    
for r, s in enumerate(e) : # Con la función "enumerate" podemos iterar sobre la posición y el valor en una lista
    print("El valor de", s, "ocupa la posición", r)
    
for r, s in zip(e, f) :
    print("El valor es", r, "en la primera lista y es", s, "en la segunda lista")
    
for r in reversed(range(11)) : # Con la función "reversed" podemos invertir una lista
    print("Quedan", r, "segundos")
    
for r in sorted(n) : # Con "sorted" podemos ordenar una lista
    print(r)
    




# Más sobre operadores

# Operadores de comparación
"Masa" in n # Verifica si el objeto está en una secuencia
"Masa" not in n
e is f # Verifica si los objetos mutables (como listas) son iguales. Equivalente a = y != para otros objetos
e is not f
# (not) in, is (not)  y el resto de operadores de comparación (<,>,==,!=) tienen menor prioridad que operadores numéricos, y la misma entre ellos
3 < 4 == 0 # Las comparaciones se pueden encadenar. Compara si 3 es menor a 4 y si 4 es igual a 0

# Operadores booleanos
True and False
True or False
not True
True and not False or False # Equivalente a (True and (not False)) or False. "not" tiene la mayor prioridad, seguido de "and" y por último "or"
# Los operadores booleanos tienen menor prioridad que los operadores de comparación





[1, 2, 3] < [1, 2, 4] # La comparación entre secuencias es de forma lexicográfica: primero se comparan los primeros items, si son iguales se sigue con los siguientes

[1, 3, 4] < [2, 2, 3]

"a" < "b" # Para cadenas de carácteres se usa el orden ASCII

[1, 2] < [1, 2, 3] # Subsecuencias inciales son consideradas menores que la secuencia completa

[2, 3] > [1, 2, 3]

[1, 2, 3] == [1, 2, 3] # Si todos los elementos de una secuencia son iguales, las secuencias serán iguales

[1, 2, 3] < "abc" # Distintos tipos de objeto no se pueden comparar