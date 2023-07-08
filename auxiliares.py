from datetime import datetime
import csv

#verifica que el numero de router ingresado por el usuario sea valido
def verificarNumeroRouter(numeroRouter, ruta):
    if numeroRouter in range (1, ruta.len+1):
        return True
    else:
        return False

#escribe en el archivo system_log.csv recibiendo como parametro el estado del router y el numero de router
def escribirEnLog(accion, numeroRouter):
    with open('system_log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ROUTER_"+str(numeroRouter), datetime.now(), accion])
    
#verifica que el numero de router ingresado por el usuario sea menor a la cantidad de routers en la ruta
def validarRouterDestinoMenorATotalRouters(destino, ruta):
    if destino in range (1, ruta.len):
        return True
    else:
        return False
    
#verifica que el input ingresado por el usuario sea un numero
def verificarNumeroInput(texto1):
    while True:
        varStr = input(texto1)
        try:
            varInt = int(varStr)
            if varInt!=None:
                break
            else:
                print("Ingreso invalido. Por favor, inténtelo de nuevo.")
        except ValueError:
            print("Ingreso invalido. Por favor, inténtelo de nuevo.")
    return varInt