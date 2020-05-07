import os

from manejadorLibros import manejadorLibros

from claseMenu import Menu

if __name__ == '__main__':
    libros = manejadorLibros()

    libros.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print("0 Salir\n1 Inciso 1\n2 Inciso 2")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0
