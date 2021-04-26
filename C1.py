# -*- coding: utf-8 -*-

# La línea de arriba es importante pues le señala a Ptyhon la codificación del script. Por ejemplo, así puede manejar en este caso carácteres con tildes

# 1 - Introducción





# Escribiendo # se pueden hacer comentarios en el script





2+2 # Podemos mostrar resultados de operaciones o funciones en la consola





x = 2+2 # Creamos el objeto "x" asignándole el número 4. El valor no será mostrado en la consola

x # Lo mostramos en la consola





x = 6 # Podemos reemplazar su valor

x





y = 2*10

y





z = x+y # Podemos crear objetos a partir de otros

z






# Hay distintos tipos de objetos






a = 6 # Tipo Entero

a

type(a) # Para ver el tipo de objeto se usa la función type()

help(type) # Con help() puedes ver la documentaciones de funciones y módulos.





b = 3.045 # Tipo Flotante

b

type(b)





c = a+b # Cuando operamos objetos compatibles pero de distinto tipo, python automáticamente los convertirá en el tipo más adecuado. Por ejemplo, sumar un entero y un flotante resultará en un flotante

c

c = 6/3 # Cuando dividimos usando "/", la operación es división flotante: el resultado se expresará como flotante

c

type(c)

c = 6//3 # Si queremos un resultado como entero, usamos "//" para división entera

c

type(c)

c = 10//4 # Usar división entera en un resultado no entero, el resultado resultará truncado

c





d = 3+7j # Tipo Complejo (sirve tanto "j" como "J")

d

type(d)






d = complex(3,7) # También podemos crear complejos usando la función complex()

d

d.real # Y acceder a su componente real e imaginario con .real y .imag

d.imag

d.conjugate() # Y su conjugado





a = float(a) # float() convierte el objeto en flotante. Lo mismo con int()

a

type(a)

a = int(a)

a

type(a)





abs(-8) # abs() sirve para obtener el valor absoluto de un número

10%6 # Usamos la operación "%" para obtener el resto de una división






# Podemos expresar números en bases distintas a la decimal

e = 0o17 # Base octal. Se usa el prefijo "0o" o "0O"

e # La consola lo expresa en base decimal

e = 0xF # Base hexadecimal. Se usa el prefijo "0x" o "0X"

e

e = 0b1111 # Base binaria. Se usa el prefijo "0b" o "0B"

e




_ # Python guarda en "_" el último valor mostrado en la consola

f = _*5

f





g = "Hola. ¿Cómo estás?" # Tipo cadena. Sirve para guardar cadenas de caractéres, usando doble comillas " o comillas simples '.

g





h = "McDonald\'s saca al mercado su \"Big Mac\"" # Para poner caracteres especiales, es necesario anteponer un "\".

h

h = "Esta paya amigos míos, \
será la última de la noche, \
ahora vayan a acostarse, \
y déjense de hacer boche."

h # Al escribir una cadena de texto en varias líneas, es necesario poner "\" al final, para indicar que lo que va abajo es una continuación de la cadena. Sin embargo, no se añade un salto de línea.

h = "Esta paya amigos míos, \n\
será la última de la noche, \n\
ahora vayan a acostarse, \n\
y déjense de hacer boche."

h # Se debe incluir "\n" para añadir saltos de línea. Sin embargo, es necesario usar la función print() para que se efectúe

print(h)

h = r"Esta paya amigos míos, \n\
será la última de la noche, \n\
ahora vayan a acostarse, \n\
y déjense de hacer boche."

h # Al añadir "r" antes de la cadena, a esta se le añade "\" antes de los caracteres especiales...

print(h) # ... para que print() los muestre en la consola. Esto se le llama cadena cruda.

h = """Esta paya amigos míos, 
será la última de la noche, 
ahora vayan a acostarse, 
y déjense de hacer boche."""

h # Al usar triple comillas (dobles o simples) se añaden automáticamente saltos de líneas

print(h)





a # Nótese que al correr las siguientes líneas al mismo tiempo, solo se mostrará el último valor en la consola, pues los valores se han puesto directamente
b
c
d
e
f
g
h

print(a) # print() evita esto
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h) # Nótese que print() expresa cadenas de texto sin comillas

print("Tengo", a, "ovejas") # Además, permite expresar snetencias mezclando cadenas de texto con valores





i = "¿Cómo" + " estás?" # Puedes realizar ciertas operaciones con cadenas. Por ejemplo, unirlas con "+"

i

i = "¿Cómo" " estás?" # O sin "+"

i = "¿Cómo estás?"*5 # O repetir cadenas con "*"

i





j = "Paralelepipedo"

j[5] # Podemos acceder a un elemento de la cadena señalando su posición entre corchetes "[]" con un entero.

j[0] # La indexación parte con 0

j[0:5] # Podemos seleccionar un intérvalo señalando la posición inicial y final separadas con ":". Nótese que el último carácter no es seleccionado

j[6:] # Si no se especifica una posición...

j[:6]

j[:]

j[0] = "p" # No podemos reemplazar un elemento de la cadena directamente. Esto nos dará error.

j = "p" + j[1:]

j[0:100] # Podemos ver como Python trabaja con índices poco lógicos

j[50:60]

j[4:2]

j[100] # Esto nos da error

j[-1] # Sin embargo, con índices negativos, Python lee desde la derecha

j[-5:-1]

j[-1:-5]

j[-0]

j[-50:]

j[-60:-50]

j[-100]

len(j) # Podemos ver la longitud (cantidad de elementos) de una cadena con len()





k = "un saludo para todos." # Existen distintos "métodos" para trabajar con cadenas. Aquí hay algunos, pero son muchos más (https://www.w3schools.com/python/python_ref_string.asp)

k

k.capitalize()

k.count("a")

k.find("l")

k.replace("todos","nadie")

k.upper()





l = True # Tipo booliano. Toma dos posibles valores: Verdadero (True) y Falso (False)

l

l = 4>2 # Podemos definir un objeto booliano a través de una condición. ">": mayor que

l

l = 7==9 #"==": igual que

l





m = [5 , 6.57 , False , "Hola hola" , 89] # Tipo lista. Objeto compuesto de otros objetos, encerrados en "[]" y separados por ",". Nótese que objetos pueden ser de distintos tipos

m

m[1] # Podemos seleccionar elementos de la lista a través de índices de la misma forma que con cadenas de texto

m[0:3]

m[-2]

m

m[0] = 9 # Pero a diferencia de cadenas de texto, se puede reemplazar directamente el elemento de una lista.

m

m[3:3] = ["Saludos", 34] # Podemos agregar términos

m

m[5:6] = [] # También eliminarlos

m

m[:2] + [True] + m[3:] # Las operaciones de cadenas se mantienen

m + [False , 9.57] 

m*3

len(m)





n = ["e" , 23 , False , True , m , 56.68 , 12] # Podemos concatenar listas

n

len(n) # Longitud de la lista original

len(n[4]) # Longitud de la lista dentro de la lista original

n[4] # Elemento de la lista original

n[4][3] # Elemento de la lista dentro de la lista original

n[4][3][2] # Elemento de la cadena de texto dentro de la lista dentro de la lista original