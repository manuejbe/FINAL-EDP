#Calcular la tasa de paquetes que cada router del sistema procesó (diferenciando en reenvío y recepción final), informando el resultado por consola.

#la cantidad de paquetes reenviados se calculan como los recibidos menos los destinados a este router
#la cantidad de paquetes destinados a este router se calculan como la cantidad de paquetes que tenian como router de destino a este router

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
        