# -*- coding: utf-8 -*-

def mult(*args) :
    """ Multiplica de forma ineficiente """
    a = 1
    for i in range(len(args)) :
        a = a*args[i]
    return a