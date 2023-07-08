#Calcular la tasa de paquetes que cada router del sistema procesó (diferenciando en reenvío y recepción final), informando el resultado por consola.

def tasaPaquetes(routingSim):
    router = routingSim.ruta.head
    for i in range(routingSim.ruta.len):
        router=routingSim.ruta.accederNodo(i+1)
        cantDestinados=len(router.paquetesDestinados)
        cantRecibidos=router.paquetesRecibidos
        print("Calculo de tasas para cada paquete")
        print("Router: ", router.posicion)        
        print("Tasa de paquetes reenviados: ", str((cantRecibidos-cantDestinados)/routingSim.duracionSimulacion) + " paquetes/segundo")
        print("Tasa de paquetes destinados a este router: ", str(cantDestinados/routingSim.duracionSimulacion) + " paquetes/segundo")
        