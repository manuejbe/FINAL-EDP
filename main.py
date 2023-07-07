from clases.Ruta import *
from clases.Router import *
from opcionesMenu import *
from auxiliares import *
import tracemalloc

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
                activarRouter()
            case 3:
                desactivarRouter()
            case 4:
                mostrarRuta(ruta1)
            case 5:
                await simularRuta(ruta1)
            case 6:
                termina=True


#ejecucion del programa principal
nombreRuta="Ruta1"
ruta1 = Ruta(nombreRuta)
with open('system_log.csv', 'w') as f:
    f.write("")
    f.close()
ruta1.inicializarRutaRandom()
asyncio.run(menu())