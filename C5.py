# -*- coding: utf-8 -*-

# 5 - Formato de texto y escritura de archivos





a = "Saludos terrícolas."

str(a) # Devuelve un valor convertido en cadena de texto de forma legible para el usuario final

repr(a) # Devuelve cadenas de texto que pueden ser leídas por el intérprete. Nótese que en este vaso devuelve una cadena de texto con la cadena de texto al interior

print(str(a))

print(repr(a))

a = 0.5

str(a)

repr(a) # al usar números, entregan el mismo valor




for b in range(1,11) :
    print(repr(b).rjust(2), repr(2*b).rjust(5,"-"), repr(b**3).ljust(10,"*"), repr(b-10).center(5,"+"))

# Los métodos "rjust", "ljust", "center" permiten justificar la cadena de texto en una cantidad de espacio determinada por su argumento. Como argumento opcional podemos incluir el relleno, que por default es " ".

# Nótese también que "print()" incluye espacios entre sus argumentos
    




"50".zfill(3) # Otro método relacionado es "zfill", que rellena cadenas de texto numéricas con ceros

"50".zfill(7)

"-60.45".zfill(8)





print("Mi cumpleaños es el {} de {} de {}".format(10, "Enero", "1995")) # Un método importante para cadenas de texto es "format", que reemplazará los valores en la cadena con cierto formato

print("Mi cumpleaños es el {1} de {2} de {0}".format(10, "Enero", "1995")) # Se puede cambiar el orden

print("Mi cumpleaños es el {dia} de {mes} de {año}".format(dia = 10, mes = "Enero", año = "1995"))

print("Mi cumpleaños es el {1} de {0} de {año}".format(10, "Enero", año = "1995"))

print("Tengo {0:.4f} segundos para {2:10} el número {1:20d}".format(0.123456789, 4567, "escribir")) # Se puede especificar formato con un ":" despues del arugmento posicional.

c = { "Martín" : 25 , "Nicolás" : 26 , "Jose" : 30 }

print("Martín tiene {0[Martín]} años, Nicolás tiene {0[Nicolás]} años y Jose tiene {0[Jose]} años".format(c)) # Se puede tratar de esta forma al ingresar un diccionario

print("Martín tiene {Martín} años, Nicolás tiene {Nicolás:7d} años y Jose tiene {Jose:15} años".format(**c)) # Desempaquetando el diccionario también se puede





d = open("scripts\\python\\ARCHIVO1.txt", "r") # "open()" sirve para abrir archivos. El primer argumento corresponde al nombre del archivo. El segundo corresponde al modo en que se abrirá. "r" corresponde al modo de lectura, "w" al modo escritura (borrará archivo existente) y "a" es para agregar información al final del contenido ya existente. "r+" abre en modo de lectura y escritura. "r" va por defecto

# Para archivos que no son de texto, sirve agregar "b" al modo para abrir el archivo en modo binario

type(d)

d

d.close() # El método "close" sirve para cerrar el archivo





with open("scripts\\python\\ARCHIVO1.txt", "r") as d : # Usar "with" permite cerrar de manera correcta el archivo una vez terminado su uso
    e = d.read() # El método "read" sirve para leer el archivo y devolverlo en cadena de texto
 
e  

d.closed # El método "closed" permite saber si el archivo está cerrado  

d.read() # Esto tirará error: el archivo ya se cerró
    
with open("scripts\\python\\ARCHIVO1.txt", "r") as d :
    f = d.readline() # "readline" lee una línea y pasa a la siguiente
    g = d.readline()
    h = d.readline()
    i = d.readline()

f

g

h

i

with open("scripts\\python\\ARCHIVO1.txt", "r") as d :
    for k in d : # Otra forma de tratar las líneas es con loops sobre el archivo
        print(k)

with open("scripts\\python\\ARCHIVO1.txt", "r") as d :
    l = d.readlines() # O se pueden guardar en una lista
    
l





with open("scripts\\python\\ARCHIVO2.txt", "w") as m : # Si el archivo no existe, Python lo crea
    m.write("Saludos terrícolas\n") # Para escribir en el archivo, se usa el método "write"
    n = m.tell() # Devuelve la posición en el archivo
    m.write(str(234)) # Es necesario pasar todo valor escrito a cadena de texto
    o = m.tell()
    
n

o

m = open("scripts\\python\\ARCHIVO2.txt", "w")

m.write("¡Soy el ser más poderoso del mundo.")

m.tell()

m.seek(24) # El método "seek" modifica el punto de referencia, donde su primer argumento es el desplazamiento desde el inicio. Además, devuelve la posición resultante

m.tell()

m.write(" y guapo del mundo!")

m.close()

with open("scripts\\python\\ARCHIVO2.txt", "r") as m :
    p = m.read()

p

m.close()

import os

os.remove("scripts\\python\\ARCHIVO2.txt") # Aprovecho de eliminar el archivo con os.reamove()