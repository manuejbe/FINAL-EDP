from datetime import datetime
import csv

def verificarNumeroRouter(numeroRouter, ruta):
    if numeroRouter in range (1, len(ruta.routers)):
        return True
    else:
        return False
    
def escribirEnLog(accion, numeroRouter):
    with open('system_log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ROUTER_"+str(numeroRouter), datetime.now(), accion])
    
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