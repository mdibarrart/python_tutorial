# -*- coding: utf-8 -*-

# 7 - Más sobre clases





a = [1, 2, 3, 4, 5]

b = "abcde"

for c in a : # Vamos a profundizar sobre la iteración en objetos
    print(c)
    
for c in b :
    print(c)
    
d = iter(a) # La sentencia "for", aplica la función "iter()" al objeto

d = a.__iter__() # Esto es lo mismo que lo de arriba: "iter()" simplemente aplica el método "__iter__()" del tipo de objeto en cuestión

type(d)

e = iter(b)

type(e)

d.__next__() # El objeto de iteración define el método "__next__", que le permite acceder al siguiente item de la iteración, el cual es aplicado continuamente por la sentencia "for" para obtener el elemento a usar en los comando asociados

d.__next__()

d.__next__()

d.__next__()

d.__next__()

d.__next__() # Cuando no quedan items a iterar, el método levanta una excepción StopIteration

e.__next__()

e.__next__()

e.__next__()

e.__next__()

e.__next__()

e.__next__()

# Pordemos entonces crear comportamientos de iteración a las clases: tenemos que crearles un método "__iter__()" que cree un objeto con el método "__next__()"

class ZergUnit() :
    def __init__(self,nombre, ps, ataque, armadura, habilidad):
        self.stats = { "Nombre" : nombre, "Puntos de salud" : ps, "Ataque" : ataque, "Armadura" : armadura, "Habilidad" : habilidad}
        self.index = len(self.stats)
        
    def __iter__(self) : # Podemos crear el método "__iter__()" para devolver el objeto con el método "__next__()". En este caso, este último se ubica en la misma clase, asi que podemos ertornar la propia instancia
        return self
    
    def __next__(self) : # Acá hacemos que usar "for", itere sobre las estadísticas de la instancia. Además, se hará en orden inverso al ingresado.
        if self.index == 0 :
            raise StopIteration
        self.index = self.index - 1
        return self.stats[list(self.stats)[self.index]]

f = ZergUnit("Zergling", 35, 5, 0, "Nacer de a 2")

iter(f)

for g in f :
    print(g)
    
def h(unit) : # Los generadores son funciones que permiten crear iteradores de forma más simple
    for index in range(len(unit)-1,-1,-1) :
        yield list(unit)[index] # La gracia está en el uso de la sentencia "yield", que permite obtener data una a la vez
        
for i in h(f.stats) : # De esta forma se aplica un generador
    print(f.stats[i])





print(f) # Cuando usamos "print()" en nuestra clase, muestra un output que tal vez no sea el que queramos

str(f)

repr(f)

class ZergUnit() :
    def __init__(self,nombre, ps, ataque, armadura, habilidad) :
        self.stats = { "Nombre" : nombre, "Puntos de salud" : ps, "Ataque" : ataque, "Armadura" : armadura, "Habilidad" : habilidad}
    def __repr__(self) : # Con el método "__repr__" señalamos qué queremos que devuelva la función "repr()" cuando se aplica a una instancia de la clase
        return "ZergUnit(\"{0[Nombre]}\",{0[Puntos de salud]},{0[Ataque]},{0[Armadura]},\"{0[Habilidad]}\")".format(self.stats)
    def __str__(self) : # Análogo para "__str__()". Si no existe este método se tomará en cuenta el output de "repr()" cuando se usa "str()"
        return "Unidad de Raza Zerg\n\
    Nombre : {0[Nombre]}\n\
    Puntos de Salud : {0[Puntos de salud]}\n\
    Ataque : {0[Ataque]}\n\
    Armadura: {0[Armadura]}\n\
    Habilidad: {0[Habilidad]}".format(self.stats)
         
f = ZergUnit("Zergling", 35, 5, 0, "Nacer de a 2")

f

print(repr(f))

print(str(f))





1+2

"a"+"b" # La operación de suma se comporta distinta según el tipo de objeto

int.__add__(1,2) # Esto es porque cada tipo tiene su método "__add__()", el cual es llamado usando "+"

str.__add__("a","b")

class ZergUnit() :
    def __init__(self,nombre, ps, ataque, armadura, habilidad) :
        self.stats = { "Nombre" : nombre, "Puntos de salud" : ps, "Ataque" : ataque, "Armadura" : armadura, "Habilidad" : habilidad}
    def __add__(self,other) : # Ya que este método usa dos instancias, también es necesario meter el argumento "other" (por convención)
        return {"Nombre" : "Híbrido "+self.stats["Nombre"]+"-"+other.stats["Nombre"],"Puntos de salud" : self.stats["Puntos de salud"]+other.stats["Puntos de salud"], "Ataque" : self.stats["Ataque"]+other.stats["Ataque"], "Armadura" : self.stats["Armadura"]+other.stats["Armadura"],"Habilidad" : [self.stats["Habilidad"],other.stats["Habilidad"]]}
    def __len__(self) : # Así mismo, podemos crear el método "__len__()" para poder usar la función "len()" en nuestra clase
        return self.stats["Puntos de salud"]+self.stats["Ataque"]+self.stats["Armadura"]

m = ZergUnit("Zergling", 35, 5, 0, "Nacer de a 2")

n = ZergUnit("Hidralisco", 80, 10, 0, "Disparar tanto a unidades aéreas como terrestres")

m+n

len(m)

len(n)

# Estos métodos especiales, rodeados por "__" se denominan métodos dunder. Una lista de estos se puede encontrar en https://docs.python.org/3/reference/datamodel.html#special-method-names





class TerranHero() :
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido
        self.mail = nombre + "." + apellido + "@terran.com"

o = TerranHero("Jim","Raynor")

o.nombre

o.mail

o.nombre = "Sarah"

o.nombre

o.mail # Si un atributo es creado a partir de otro, este no cambiará si es que el atributo del cual se deriva cambia

class TerranHero() :
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido
    def mail(self) : # Una posible solución sería definir la variable como un método
        return self.nombre + "." + self.apellido + "@terran.com"

o = TerranHero("Jim","Raynor")

o.mail()

o.nombre = "Sarah"

o.mail() # Si bien funciona esta solución, es cierto que habrá que modificar la llamada del atributo ahora como método, lo que significará cambiar el código

class TerranHero() :
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido
    @property # Añadir el decorador "property" permitirá llamar al método como si fuera un atributo, así, no tenemos que cambiar el código
    def mail(self) :
        return self.nombre + "." + self.apellido + "@terran.com"

o = TerranHero("Jim","Raynor")

o.mail

o.nombre = "Sarah"

o.mail

class TerranHero() :
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido
    @property # Añadir el decorador "property" permitirá llamar al método como si fuera un atributo, así, no tenemos que cambiar el código
    def mail(self) :
        return self.nombre + "." + self.apellido + "@terran.com"
    @mail.setter # Con el decorador "setter", podemos asignar atributos desde otro, mediante la asignación. El nombre tiene que ser "@nombredelproperty.setter"
    def mail(self,email) : # Con un método del mismo nombre
        nombre, apellido = email[:-11].split(".")
        self.nombre = nombre
        self.apellido = apellido
    @mail.deleter # El decorador "deleter" funciona similar. Con este, buscamos ejecutar comandos con la función "del" sobre un método con decorador "property"
    def mail(self) :
        self.nombre = None
        self.apellido = None

o = TerranHero("Jim","Raynor")

o.mail

o.nombre

o.apellido

o.nombre = "Sarah"

o.mail

o.mail = "Jim.Kerrigan@terran.com"

o.nombre # Nótese que asignando el mail hemos a la vez asignado el nombre y el apellido

o.apellido

del o.mail

print(o.nombre)

print(o.apellido)





