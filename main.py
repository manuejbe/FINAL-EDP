from clases.Ruta import *
from clases.Router import *
import re

def verificarNombreRouter(nombre):
    patron = r'^router_\d+$'
    if re.match(patron, nombre):
        return True
    else:
        return False

def agregarRouterARuta(ruta: Ruta):
    nombreRouter=input("Ingrese el nombre del router que desea agregar siguiendo con el formato router_X siendo X un numero o Z para volver al menu: ")
    if nombreRouter == "Z":
        menu()
    while not verificarNombreRouter(nombreRouter):
        nombreRouter=input("El nombre no cumple con el formato router_X siendo X un numero. Ingrese el nombre del router que desea agregar nuevamente o Z para volver al menu: ")
        if nombreRouter == "Z":
            menu()
    router=Router(nombreRouter)
    ruta.agregarRouter(router)
    
def activarRouter(ruta: Ruta):
    nombreRouter=input("Ingrese el nombre del router que desea activar siguiendo con el formato router_X siendo X un numero o Z para volver al menu: ")
    if nombreRouter == "Z":
        menu()
    while not verificarNombreRouter(nombreRouter):
        nombreRouter=input("El nombre no cumple con el formato router_X siendo X un numero. Ingrese el nombre del router que desea activar nuevamente o Z para volver al menu: ")
        if nombreRouter == "Z":
            menu()
    #aca habria q encontrar el router en la lista de routers de la ruta y activarlo

def desactivarRouter(ruta: Ruta):
    nombreRouter=input("Ingrese el nombre del router que desea desactivar siguiendo con el formato router_X siendo X un numero o Z para volver al menu: ")
    if nombreRouter == "Z":
        menu()
    while not verificarNombreRouter(nombreRouter):
        nombreRouter=input("El nombre no cumple con el formato router_X siendo X un numero. Ingrese el nombre del router que desea desactivar nuevamente o Z para volver al menu: ")
        if nombreRouter == "Z":
            menu()
    #aca habria q encontrar el router en la lista de routers de la ruta y desactivarlo

def mostrarRuta(ruta: Ruta):
    if len(ruta.routers) == 0:
        print("La ruta no tiene routers")
    else:
        print("La ruta tiene los siguientes routers:")
        for router in ruta.routers:
            print(router)

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
        agregarRouterARuta()
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
menu()