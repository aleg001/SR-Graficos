"""
Autor: Alejandro Gómez
Fecha de última modificación: 14/07/22

"""
from gl import *


# Librerías para el título
import time
import sys

from SoftwareRenderer import *


# Funciones para el menu:
def Opciones():
    menuOp = input("1) SR4\n2) Salir\n")
    menuVer = verificarNum(menuOp)
    return menuVer


def verificarNum(input):
    try:
        val = float(input)
        return val
    except ValueError:
        try:
            val = int(input)
            return val
        except ValueError:
            print("¡Solamente números!")


# Mensaje de despedida
def bye():
    print("¡Gracias por usar el programa!!")


Bienvenida = "\n----- GL Library----\n"
procesando = "Procesando solicitud..."


def ImpresionTitulo(string):
    # Se imprime el título con efecto de typewriter
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)


ImpresionTitulo(Bienvenida)
menu = False
while menu == False:
    opcion = Opciones()

    if opcion == 2:
        print("Gracias por utilizar este programa.")
        print("\n")
        menu = True

    if opcion == 1:
        tituloArchivo = input("Ingrese el nombre para el archivo: ")
        tituloArchivo = tituloArchivo + ".bmp"
        ImpresionTitulo(procesando)
        SoftwareRender4(tituloArchivo)
        print("\n\n¡Imagen generada!\n")
