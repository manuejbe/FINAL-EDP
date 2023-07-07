from clases.Ruta import *
from clases.Router import *
from opcionesMenu import *
from auxiliares import *

def menu():
    print("1. Agregar router a ruta")
    print("2. Activar router")
    print("3. Desactivar router")
    print("4. Mostrar ruta")
    print("5. Simular ruta")
    print("6. Salir")
    opcion = verificarNumeroInput("Ingrese una opcion: ")
    while opcion not in range(1,7):
        opcion = verificarNumeroInput("Ingrese una opcion valida: ")
    if opcion == 1:
        agregarRouterARuta(ruta1)
    elif opcion == 2:
        activarRouter()
    elif opcion == 3:
        desactivarRouter()
    elif opcion == 4:
        mostrarRuta(ruta1)
    elif opcion == 5:
        simularRuta(ruta1)
    elif opcion == 6:
        quit()
    menu()

#ejecucion del programa principal
nombreRuta="Ruta1"
ruta1 = Ruta(nombreRuta)
ruta1.inicializarRutaRandom()
menu()