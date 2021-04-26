# -*- coding: utf-8 -*-

# 9. Decoradores





def a(nombre) :
    return "Saludos "+nombre
    
a("Nicolás")

type(a("Nicolás"))

type(a) # Nótese que las funciones son un tipo de objeto. Es distinto "function" que "function()"





def b(nombre) :
    return "Hasta luego "+nombre

b("Nicolás")

def c(func) :
    return func("Martín") # Nótese que la función espera una función como argumento

c(a)

c(b)





def d() :
    def e() : # Nótese que definimos una función dentro de otra
        print("Saludos")
    e()
    
d() # Recordando los scopes, esta solo podrá ser accedida desde el local scope

e() # Por eso, esto devolverá error

def d() :
    def e() : # Nótese que definimos una función dentro de otra
        print("Saludos")
    return e # Podemos hacer que el output de una funcion sea una función

d()

f = d() # Podemos asignarla a otro nombre para usarla después

f()





def g(func) : # Aquí creamos un decorador, el cual toma una función como argumento
    def wrapper() : # La cual define una función wrapper (no necesariamente se tiene que llamar "wrapper")
        print("Decoración añadida")
        func() # La función argumento es usada de alguna forma en el wrapper
    return wrapper # El wrapper es devuelto

def h() :
    print("Función fome que le falta algo")

h()

h = g(h) # Podemos decorar nuestra función original con el decorador

h() # El comportamiento de la función ha cambiado

@g # Usando "@decorador" podemos decorar funciones más rápido
def h() :
    print("Función fome que le falta algo")

h()





@g
def a(nombre) :
    return "Saludos "+nombre

a("Martín") # Nótese que no pudimos decorar esta función, pues esta última tiene un argumento como input

def g(func) :
    def wrapper(*args, **kwargs) : # Añadiendo "*args" y "**kwargs" podemos hacer que el "wrapper" acepte una cantidad indefinida de argumentos
        print("Decoración añadida")
        func(*args, **kwargs)
    return wrapper

@g
def h() :
    print("Función fome que le falta algo")

@g
def a(nombre) :
    return "Saludos "+nombre

h()

i = a("Martín")

print(i) # Nótese que sin embargo, la función decorada no está devolviendo el valor que entrega la función original

def g(func) :
    def wrapper(*args, **kwargs) :
        print("Decoración añadida")
        func(*args, **kwargs)
        return func(*args, **kwargs) # Arreglamos el "wrapper" para que devuelva los valores de la función
    return wrapper

@g
def a(nombre) :
    return "Saludos "+nombre

i = a("Martín")

print(i)





def k() :
    print("Saludos mortales")
    
k # Nótese que los objetos tienen la capacidad de conocer sus propios atributos, como por ejemplo su propio nombre y documentación en el caso de las funciones

k.__name__

help(k)

@g
def k() :
    print("Saludos mortales")
    
k # Nótese que al aplicar un decorador, los atributos del objeto original se mezclan con los del wrapper

k.__name__

help(k)

import functools # El módulo "functools" trae una serie de herramientas útiles para la programación de funciones

def g(func) :
    @functools.wraps(func) # El decorador "functools.wraps()" permite mantener intactos estos atributos al decorar
    def wrapper(*args, **kwargs) :
        print("Decoración añadida")
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@g
def k() :
    print("Saludos mortales")
    
k

k.__name__

help(k)