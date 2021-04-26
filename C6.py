# -*- coding: utf-8 -*-

# 6 - Manejo de errores y excepciones





# Error de sintaxis

while True print("Hola") # Falta ":" antes del "print()", por lo que Python no puede ejecutar el comando

# Se señala la línea y el lugar donde se detecta el error. También el archivo en caso de que sea un programa externo





# Otros tipos de errores

1/0 # Este es un error de división por cero

"a" + 3 # Este es un error de tipos: no se puede sumar una cadena de texto con un entero

a # Error de nombre: no está definido el objeto "a"

# Se señala la línea del error, así como el tipo de error: ZeroDivisionError, TypeError y NameError, respectivamente

# Sin embargo, no son errores de sintaxis




while True:
    try : # La sentencia "try" intenta correr los comandos asociados
        b = int(input("Ingrese un divisor para el número 10: "))
        print("El resultado es:", 10/b)
        break
    except ZeroDivisionError : # Si se genera un error particular, la sentencia "except" permite saltar los comandos siguientes de "try" y ejecutar otros comandos dada la excepción
        print("¡No se puede dividir por cero!")
    except ValueError :
        print("Por favor ingresar un número.")
        
while True:
    try :
        b = int(input("Ingrese un divisor para el número 10: "))
        print("El resultado es:", 10/b)
        break
    except : # Se puede omitir la excepción para tomar en cuenta cualquiera
        print("¡Por favor ingresar un número distinto de cero!")

try :
    b = int(input("Ingrese un divisor para el número 10: "))
except : 
    print("Se ha generado un error:")
    raise # "raise" permite mostrar la excepción generada
else :
    print("El resultado es:", 10/b) # También se puede incluir un bloque con "else", que contenga los comandos a ejecutar cuando no se genera la excepción





try :
    b = int(input("Ingrese un divisor para el número 10: "))
    print("El resultado es:", 10/b)
except (ZeroDivisionError, ValueError) : # Se pueden señalar más de una excepción en una tupla
    print("¡Error!")

try :
    b = int(input("Ingrese un divisor para el número 10: "))
    print("El resultado es:", 10/b)
except ZeroDivisionError as c: # Con "as" podemos guardar los argumentos de la excepción
    print("¡Error!")
    print(type(c))
    print(c)





raise Exception("Algo malo acaba de pasar") # "raise" permite forzar errores

try :
    d = int(input("¿Eres inteligente?\n 1 : Sí \n 2 : No \n Respuesta: "))
    if d == 1 :
        raise NameError("No mientas.")
    elif d != 2 :
        raise ValueError # Recordar que si "raise" levanta un error abordado por un "except", se correran los comandos del "except"
except ValueError :
    print("Respuesta no válida")
    raise # Este último "raise" muestra la excepción generada





class UltimateError(Exception) : # Se pueden definir errores creando una clase (se verá más adelante) derivada de la clase "Exception"
    def __init__(self, valor) : # Se crea el atributo de "valor"
        self.valor = valor
    def __str__(self) :
        return repr(self.valor)

try :
    raise UltimateError("Que wea")
except UltimateError as e :
    print(e.valor, "está pasando.")




def g(x) :
    try :
        f = 10/x
    except ZeroDivisionError : 
        print("No se puede dividir por cero.")
    else :
        print("El resultado es:", f)
    finally : # La sentencia "finally" ejecuta sus comandos independiente del resultado del "try". Ya sea haya una excepción o no. Sn embargo, en caso de que haya una excepción no manejada por "except", se lanza la excepción posterior al "finally"
        print("Que difícil es esto de programar")

g(3)

g(0)

g("a")