# -*- coding: utf-8 -*-

# 7 - Clases





# SCOPES





# Para entender mejor Python, es necesario entender la jerarquía existente a la hora de asociar nombres con objetos.
#
# El "scope" (la mira) de un nombre corresponde al area del texto en un programa donde puedes, de forma inambigua, acceder a ese nombre (de un objeto, función, etc.)
#
# Los niveles existentes de scopes son:
#
# 1 : Local      --> Corresponde a bloques dentro de la definición de una función. Aquí se pueden acceder a los nombres definidos dentro de la función
# 2 : Enclosing  --> Cuando hay funciones anidadas, si el local scope es la definición de una función intermedia, el enclosing scope corresponde a la definición de la función englobadora
# 3 : Global     --> Es el scope superior en un programa. Contiene todos los nombres definidos a nivel superior, y que pueden ser accesibles en cualquier segmento del código
# 4 : Built-in   --> Es un scope especial que es creado cada vez que se abre el editor o se corre un script. Contiene nombres especiales integrados a Python
#
# Los scopes acceden a diccionarios: conjunto de nombres asociados a valores respectivos. Estos diccionarios corresponden a namespaces





a = "a global" # "a" es creada en el scope global, pues está definida en el código principal

print(a)

def f() :
    b = "b local" # Por otra parte, "b" es una variable creada en el scope local de la función, pues se ha definido dentro de esta última
    print(b)
    
f() # Al correr la función, esta sí imprimirá la variable "b" al estar dentro del local scope (son comandos dentro de la función)

print(a) # También se imprimirá la variable "a" pues estamos en el código principal, y por ende podemos acceder a esta al estar en el global scope

print(b) # SIN EMBARGO, desde el código principal no podremos acceder a la variable "b", pues esta fuera de "la mira". Estando en el global scope no podemos acceder a variables dentro del local scope

def f() :
    print(a)

f() # NÓTESE que si bien no se ha definido una variable "a" en la función, una vez que Python no encuentra una ariable "a" en el local scope, pasa al global scope

def f() :
    a = "a local"
    print(a)

f() # Esta vez, sí se define una variable "a", por lo que la función imprimirá la variable en el local scope por tener más prioridad

print(a) # Sin embargo, en el código principal, Python buscará en el global scope

def f() :
    global a # Con el comando "global", estamos indicando a la función que estamos trabajando con la variable del global scope
    a = "a global 2"
    print(a)

f() # Por ello, tanto imprimirá el nuevo valor al correr la función...

print(a)  # ... como al imprimirla en el global scope

def f(c) : # Así mismo, argumentos introducidos son tomados como variable del local scope
    print(c)

f("c local")

print(c) # Y esto lanzará error





d = "d global"

def f() : # La relación local-global anteriormente vista es análoga a la relación local-englobadora (y englobaora-global), cuando hay funciones anidadas
    d = "d englobadora"
    def g() :
        d = "d local"
        print(d) # Se imprimirá la variable "d" creada en el local scope de la función interna
    g()
    print(d) # Dentro de la función englobadora, se imprimirá la variable "d" del enclosing scope

f()

print(d) # Y acá se imprimirá la variable del global scope

e = "e global"

def f() :
    d = "d englobadora"
    def g() :
        print(d) # No se ha definido una "d" en el local scope, por lo que buscará en el nivel inmediatamente inferior: el enclosing scope
        print(e) # Así como no se ha creado una variable "e" tanto en el local como en el enclosing scope, la función imprimirá la variable "e" del global scope
    g()
    print(d)
    print(e)

f()

print(d)

print(e)

def f() :
    def g() :
        i = "i local"
    g()
    print(i)

f() # Como es de esperarse, esta función lanzará error pues sele pide a la función englobadora que imprima una variable a la cual no tiene acceso, pues está en el local scope

def f() :
    d = "d más englobadora"
    def g() :
        d = "d englobadora"
        def h() :
            d = "d local"
            print(d)
        h()
        print(d)
    g()
    print(d)

f() # La lógica se puede extender a más niveles de scopes

print(d)

def f() :
    d = "d englobadora"
    def g() :
        nonlocal d # Con el comando nonloca, podemos acceder a las variables del enclosing scope (con global accederíamos al "d" global)
        d = "d englobadora 2"
    g()
    print(d)

f()

print(d)





min([1,2,3,4,5]) # No hemos definido la función "min()", sin embargo, podemos ejecutarla. Esto se debe a que "min()" es un atributo ubicado en el built-in scope, donde se almacenan atributos incluídos al abrir Python, y es el último nivel de scope donde Python busca, posterior al global scope

def min (k): # Podemos sobreescribirla a nivel de scope global
    print("La función ha cambiado")

min([1,2,3,4,5]) # Python buscará primero en el scope global, y luego en el scope builtin. Por ello, hay que tener cuidado al escoger nombres de variables y funciones

import builtins

print(dir(builtins)) # "dir()" muestra la lista de los atributos de un objeto, en este caso, builtins





# CLASES





# Las clases básicamente son tipos de objetos definidos por el usuario

# Hay muchas cosas que considerar respecto a estas





# 1. Clases vs Instancias

class ZergUnits : # Aquí se ha creado una clase
    pass # Eso sí, esta vacía

ZergUnits

type(ZergUnits)

class ZergUnits :
    """ Unidad de la raza Zerg """
    habilidad = "Regeneración Biológica" # Hemos creado una variable de clase (más adelante se verá que es esto)

ZergUnits.habilidad

ZergUnits.habilidad = "Madriguera" # Podemos modificar la variable de clase con asignación

ZergUnits.habilidad

ZergUnits.__doc__ # Podemos acceder a la documentación de la clase

# Lo que creamos arriba es una clase: nos detalla las características de esta

m = ZergUnits() # Cuando creamos un objeto llamando a la clase, estamos creando una instancia de la clase

m

type(m)

m.habilidad

type(m.habilidad)





# 2. Atributos, métodos, y variables de clase

# Hay tres conceptos básicos de una clase que hay que entender

# a) Atributos : Estos son variables a nivel de instancia (pueden variar a nivel de instancia)

# b) Métodos : Estos son funciones a nivel de instancia (son ejecutadas a nivel de instancia)

# c) Variables de clase : Estos son variables a nivel de clase (son iguales para todas las instancias)

class ZergUnits :
    def __init__(self, nombre, tipo) : # Estamos definiendo un método. En este caso, es un método especial llamado "__init__" que al igual que cuando se importa un módulo, esta función es ejecutada al crear una instacia
        self.name = nombre # Nótese que la función recibe un argumentl "self". Se usa "self" por convención, pero podría ser cualquier cosa. Sin embargo, es necesario incluir un primer argumento porque los métodos automáticamente toman a la instancia como primer argumento
        self.tipo = tipo # Además, ¡nótese que estamos creando un atributo! Estamos a nivel de instancia (al usar self). Para nombrar el atributo da lo mismo si se usa el mismo nombre del argumento
    habilidad = "Regeneración biológica" # Aquí estamos asignando una habilidad a nivel de clase: es una variable de clase
    def poder_especial(self, poder) :
        self.poder = poder
        

o = ZergUnits("Zergling","Terrestre")

p = ZergUnits("Mutalisco","Aérea")

o.name

p.name

o.tipo

p.tipo

o.habilidad

p.habilidad

o.__dict__ # Podemos ver el diccionario de atributos (el namespace). Nótese que no esta habilidad

ZergUnits.__dict__ # Aquí sí podemos verla, pues es una variable de clase

o.habilidad = "Madriguera"

o.habilidad # Nótese que pareciera que la variable de clase ha cambiado

p.habilidad # Pero no es así

o.__dict__ # La razón se ve aquí. Se ha creado un nuevo atributo para la instacia "o". Por ende, se concluye que Python prioriza atributos de instancia sobre variables de clase

ZergUnits.habilidad = "Madriguera" # Así se cambia la habilidad a nivel de clase

o.poder_especial

type(o.poder_especial) # Objeto método

o.poder_especial("Correr muy rápido")

o.poder

type(ZergUnits.poder_especial) # Objeto función

ZergUnits.poder_especial(p,"Disparar cositas que rebotan en las unidades enemigas") # Es necesario agregar el argumento de instancia cuando se llama la función desde la clase

p.poder





# 3. Métodos de clase y métodos estáticos

# Sabiendo que existen los métodos, que son funciones que toman a la instancia como primer argumento, surge la pregunta de si existen funciones que toman la clase como primer argumento

# Si existen, y se llaman métodos de clase

class ZergUnits :
    def __init__(self,nombre):
        self.nombre = nombre
    habilidad = "Regeneración biológica"
    @classmethod # Métodos de clase básicamente son un decorador (estos se verán más adelante)
    def cambiar_habilidad(cls,skill) : # Después del decorador, definimos nuestro método de clase, el cual tomará el primer argumento automáticamente como la clase, análogo a los métodos normales
        cls.habilidad = skill
        
o = ZergUnits("Zergling")

p = ZergUnits("Hidralisco")

o.habilidad

p.habilidad

ZergUnits.cambiar_habilidad("Madriguera") # Así se llama al métdo de clase, análogo al método normal

o.habilidad

p.habilidad

o.cambiar_habilidad("Multiplicarse como conejos") # Podemos llamar al método de clase por la instancia, lo cual tiene el mismo efecto que llamarla desde la clase, por lo cual no se hace mucho

o.habilidad

p.habilidad

class ZergUnits :
    def __init__(self,nombre,PS,ataque,armadura) :
        self.nombre = nombre
        self.PS = int(PS)
        self.ataque = int(ataque)
        self.armadura = int(armadura)
    @classmethod
    def from_string(cls, zerg_string) : # Los métodos de clase en particular pueden servir para definir constructores: formas de crear una clase a partir de otros objetos. Por ejemplo, aquí queremos crear una unidad zerg a partir de una cadena de textos con sus atributos separados por comas (algo normal por ejemplo en archivos de texto)
        name, HP, attack, armor =  zerg_string.split(",") # Creamos variables separando la string ingresada
        return cls(name,HP,attack,armor) # Retornamos la creación de la clase
    
zerg_string_1 = "Zergling,35,5,0"

zerg_string_2 = "Hidralisco,80,10,0"

o = ZergUnits.from_string(zerg_string_1)

p = ZergUnits.from_string(zerg_string_2)

o.nombre

o.ataque

p.nombre

p.ataque

class ZergUnits :
    def __init__(self,nombre) :
        self.nombre = nombre
    @staticmethod # Por último, están los métodos estáticos, los cuales simplemente no toman como primer argumento ni la instancia ni la clase
    def description() : # La función no toma como argumento ni "self" ni "cls". En este caso, la función no es muy útil
        print("Unidad")

o = ZergUnits("Zergling")

p = ZergUnits("Mutalisco")

o.description()

p.description()





# 4. Herencia y subclases

class Units() :
    def __init__(self,nombre,ps,ataque,armadura) :
        self.nombre = nombre
        self.ps = ps
        self.ataque = ataque
        self.armadura = armadura
    habilidad = "Ninguna"
    def mostrar_habilidad(self) :
        print(self.habilidad)

class Zergs(Units) : # Hemos creado una subclase a partir de una clase base, de tal forma que la primera hereda los atributos y métodos de la segunda
    pass

q = Zergs("Zergling",35,5,0)

type(q)

q.nombre

q.habilidad

q.mostrar_habilidad()

class Zergs(Units) :
    habilidad = "Regeneración biológica"
    
q = Zergs("Zergling",35,5,0)

q.habilidad # Nótese que el atributo priorizado es el de la clase derivada, a pesar de ser especificado tanto en la clase base como en la derivada

q.mostrar_habilidad() # Incluso al especificar un método en la clase base, se toma en cuenta primero los atributos de la clase derivada

class Protoss(Units) : # Suponga que para crear una instancia de una clase derivada se necesita más argumentos que los exigidos por el "__init__" de la clase base
    def __init__(self,nombre,ps,ataque,armadura,escudo) : # Podemos crear un nuevo "__init__" (recordemos que este se priorizará sobre el de la clase base)
        super().__init__(nombre,ps,ataque,armadura) # Con el prefijo "super()" estamos indicando a la superclase de la que se deriva la actual subclase
        self.escudo = escudo

r = Protoss("Zealot",100,16,1,60)

r.nombre

r.escudo

isinstance(r, Protoss) # ¿Es el primer argumento una instancia del segundo?

isinstance(r, Units) # Clases bases también son aprobadas

isinstance(r, Zergs)

issubclass(Zergs, Units) # ¿Es el primer argumento una subclase del segundo?

issubclass(Zergs, Protoss)





class Zergs() :
    habilidad = "Regeneración biológica"
    
class Protoss() :
    habilidad = "Escudo psiónico"

class XelNaga(Zergs,Protoss) : # Se pueden hacer herencias múltiples para heredar atributos de ambas clases
    pass

s = XelNaga

XelNaga.habilidad # Pero existe cierto orden de resolución de métodos para aquellos atributos/métodos de nombre compartido entre clases superiores. Este orden también es seguido por la función super()

XelNaga.__mro__ # Aquí podemos ver el orden de resolución con el atributo "__mro__"

# Cundo se trabaja con herencia múltiple, se recomienda no reusar nombres dentro de lo posible.

class ClaseBaseBase1() :
    pass

class ClaseBaseBase2() :
    pass

class ClaseBaseBase3() :
    pass

class ClaseBaseBase4() :
    pass

class ClaseBase1(ClaseBaseBase1,ClaseBaseBase2) :
    pass

class ClaseBase2(ClaseBaseBase3,ClaseBaseBase4) :
    pass

class ClaseFinal(ClaseBase1,ClaseBase2) :
    pass

ClaseFinal.__mro__ # Aquí se puede apreciar el orden de búsqueda cuando agregamos más niveles de herencia