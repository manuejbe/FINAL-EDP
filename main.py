from clases.Ruta import *
from clases.Router import *
from opcionesMenu import *
from auxiliares import *
from grafico import *
import tracemalloc
from tasa import *
import asyncio

tracemalloc.start()
async def menu():
    termina=False
    while not termina:
        print("1. Agregar router a ruta")
        print("2. Activar router")
        print("3. Desactivar router")
        print("4. Mostrar ruta")
        print("5. Simular ruta")
        print("6. Salir")
        opcionElegida=verificarNumeroInput("Ingrese la opcion deseada: ")
        while opcionElegida not in range(1,7):
            opcionElegida=verificarNumeroInput("Ingrese una opcion valida: ")
        match opcionElegida:
            case 1:
                agregarRouterARuta(ruta1)
            case 2:
                activarRouter(ruta1)
            case 3:
                desactivarRouter(ruta1)
            case 4:
                mostrarRuta(ruta1)
            case 5:
                routingSim = await simularRuta(ruta1)
                
                tasaPaquetes(routingSim)
            case 6:
                termina=True


#creacion de la ruta utilizando la clase Ruta
nombreRuta="Ruta1"
ruta1 = Ruta(nombreRuta)
#creacion del archivo system_log.csv para despues poder appendear la data
with open('system_log.csv', 'w') as f:
    f.write("")
    f.close()
#creacion de routers y agregado a la ruta (de forma aleatoria y en estados aleatorios)
ruta1.inicializarRutaRandom()
#creacion de los txts para cada router
ruta1.crearTxts()
#ejecucion del menu
asyncio.run(menu())
#creacion del grafico
graficar(ruta1)