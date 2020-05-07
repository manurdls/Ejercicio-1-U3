import os

from manejadorLibros import manejadorLibros

def opcion1():
    band = False
    while not band:
        id = int(input('Ingrese el id del libro: '))
        os.system('cls')
        if libros.buscarId(id) == True:
            band = True
        else:
            print('Error: el id ingresado no pertenece a ningun libro.')


def opcion2():
    palabra = input('Ingrese una palabra: ')
    libros.buscaPalabra(palabra)

def opcion3():
    print("Adiós")


switcher = {
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    libros = manejadorLibros()

    libros.cargarDatos()

    bandera = False
    while not bandera:
        print("\n-----------MENU-----------")
        print("1. Inciso 1")
        print("2. Inciso 2")
        print("3. Salir")
        opcion= int(input("Ingrese una opción: "))
        os.system('cls')
        switch(opcion)
        bandera = int(opcion)==3
