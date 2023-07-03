from clases.Ruta import *
from clases.Router import *
from opcionesMenu import *
from auxiliares import *
from simulacion import *

def menu():
    print("1. Agregar router a ruta")
    print("2. Activar router")
    print("3. Desactivar router")
    print("4. Mostrar ruta")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    while opcion not in ["1","2","3","4","5"]:
        opcion = input("Ingrese una opcion valida: ")
    if opcion == "1":
        agregarRouterARuta(ruta1)
    elif opcion == "2":
        activarRouter()
    elif opcion == "3":
        desactivarRouter()
    elif opcion == "4":
        mostrarRuta(ruta1)
    elif opcion == "5":
        quit()
    menu()

#ejecucion del programa principal
nombreRuta="Ruta1"
ruta1 = Ruta(nombreRuta)
simularRuta(ruta1)
menu()