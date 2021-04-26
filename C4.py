# -*- coding: utf-8 -*-

# 4 - Módulos





# La ejecución de programas largos se puede facilitar con la creación de scripts como el presente.

# Sin embargo, hay veces que ciertas definiciones (como funciones) pueden ser requeridas constantemente y convendrá entonces confeccionar módulos desde donde importarlas a nuestro script en vez de escribir las definiciones en cada archivo





import modulo_C4 # Así­ podemos importar un módulo. Si corre este comando desde Spyder u otro editor, no funcionará. Si lo corre desde la terminal, sí funcionará

import sys

sys.path # Lista que incluye todas las direcciones donde Python busca

a = "C:\\Users\\Pipo Dirrabart\\scripts\\python" # Cambiar este valor al directorio donde se ubican los scripts y módulos

if a not in sys.path : # Acá se busca agregar el nuevo directorio
    sys.path.append(a) # NOTA: este procedimiento no agrega de forma permanente la dirección en posteriores sesiones





import modulo_C4

type(modulo_C4)

modulo_C4.__name__ # Al importar un módulo su nombre se guarda en __name__ como cadena de texto

modulo_C4.f(4) # De esta forma podemos llamar a funciones

modulo_C4.g("Saludos mortales","o")

b = modulo_C4.f # Podemos asignar la función a un objeto para no tener que llamarla indirectamente

b(8)

from modulo_C4 import g # Aunque de esta forma se pueden importar las función de forma directa (no se importa el módulo)

g("Que fácil es esto","e")

from modulo_C4 import * # Así se importan todas las funciónes del módulo (que no empiecen con _)





# Un modulo integrado es "sys", que ya fue importado líneas más arriba, que contiene algunas variables relevantes integradas a Python

sys.ps1 # Cursor primario

sys.ps2 # Cursor secundario





dir(modulo_C4) # la función "dir()" genera la lista de los nombres definidos al importar el modulo

dir(sys)

dir() # Muestra todos los nombres definidos

dir(__builtin__) # Muestra funciones y variables integradas





# Un paquete es un conjunto de módulos organizados de una forma determinada

# "paqueton" es un paquete artificial, el cual tiene la siguiente estructura:
#
#
# paqueton/
#    __init__.py
#    ostia.py
#    cosasextras/
#        __init__.py
#        abcde.py
#        extras.py
#        ojoahi.py
#    formato/
#        __init__.py
#        inventadocosas.py
#        inventadocosas2.py
#    nombreguay/
#        __init__.py
#        estosigue.py
#        funcionesutiles.py
#        estosigue/
#            __init__.py
#            hastacuandoconesto.py
#            porfavornomas.py
#
#
# Una serie de cosas a destacar:
#
# - Un paquete no es un GRAN módulo, si no que un conjunto de módulos organizados
# - Hay módulos dentro de la carpeta principal, así como hay subpaquetes que incluyen en sí mismos más módulos
# - En cada subdirectorio tiene que estar un archivo __init__.py, para que Python lea el directorio como paquete. Este archivo puede estar incluso vacío
# - Cuando se importa un módulo, se crea una carpeta __pycache__, que incluirá archivos nombredemodulo_script.versiondepython.pyc, por temas de rapidez, sin entrar en conflicto cuando se cambia de versión de Python





import paqueton.cosasextras.abcde # Así se importan módulo dentro de un paquete

paqueton.cosasextras.abcde.a("¡Saludos amigos míos!")

from paqueton.cosasextras import extras # Así importamos directamente el nombre del módulo

extras.greet("Nicolás")

from paqueton.formato.inventadocosas import tripl # Así importamos directamente una función del módulo

tripl(3)

from paqueton.cosasextras import * # De esta forma, supondríamos que se importarán (de forma directa) todos los módulos del directorio señalado al usar "*"

ojoahi.mult(2,3,4,5) # Sin embargo solo estarán importados los módulos "ojoahi" y "extras" (este último además ya lo habíamos importado previamente)

abcde.b("Babosa") # Esto tirará error, pues el archivo __init__ en "cosasextras" señala que se carguen solo estos dos módulos con "*" pal definir la lista __all__ con los nombres de estos módulos