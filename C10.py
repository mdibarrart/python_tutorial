# -*- coding: utf-8 -*-

# 10. Librería Python





# OS

import os # El módulo "os" provee funciones para interactuar con el sistema operativo

dir(os) # Lista de funciones

help(os) # Manual del módulo

os.system("notepad") # Corre el comando en el terminal. En este caso, se abrirá el block de notas

os.getcwd() # Devuelve el directorio de trabajo

os.chdir("C:\\Users\\Pipo Dirrabart\\scripts\\python") # Cambia el directorio de trabajo





# MATH

import math # "math" provee herramientas matemáticas fundamentales

math.cos(0)

math.pi

math.log(64,2)

math.e





# RANDOM

import random # "random" provee funciones relacionadas con el muestreo aleatorio

random.choice(["a","b","c"]) # Elección con reemplazo

random.sample(range(100), 10) # Elección sin reemplazo

random.random() # Float al azar entre 0 y 1

random.randrange(14) # Elección de un entero entre 0 y 13 con reemplazo





# DATE

import datetime # "datetime" trae funciones para la manipulación de fechas

hoy = datetime.date.today()

hoy

nacimiento = datetime.date(1995,1,10)

nacimiento

edad = hoy - nacimiento

edad

edad.days





# Existen muchos módulos incluidos en la biblioteca estándar de Python, que pueden ser útiles. Así que se recomienda echarle un ojo