import matplotlib.pyplot as plt


def graficar(ruta):
    cantrouters=ruta.len

    routers = []
    for i in range(cantrouters):
        routers.append("Router "+str(i+1))

    #las 2 lista declaradas aca abajo van a tener numeros en cada posicion que representan la cantidad de paquetes enviados y recibidos por cada router
    paquetes_enviados = []
    paquetes_recibidos = []

    router = ruta.head
    while router != None:
        paquetes_enviados.append(router.paquetesRecibidos-len(router.paquetesDestinados)+router.contPaquetesOriginados)
        paquetes_recibidos.append(router.paquetesRecibidos)
        router = router.siguiente


    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Configurar los datos de las barras
    ancho_barras = 0.35
    posicion_routers = range(len(routers))

    # Dibujar las barras de paquetes enviados
    rects_enviados = ax.bar(posicion_routers, paquetes_enviados, ancho_barras, label='Enviados')

    # Dibujar las barras de paquetes recibidos
    rects_recibidos = ax.bar([p + ancho_barras for p in posicion_routers], paquetes_recibidos, ancho_barras, label='Recibidos')

    # Configurar el eje x
    ax.set_xticks([p + ancho_barras / 2 for p in posicion_routers])
    ax.set_xticklabels(routers)

    # Configurar las etiquetas y la leyenda
    ax.set_ylabel('Cantidad de paquetes')
    ax.set_title('Paquetes enviados y recibidos por router')
    ax.legend()

    # Mostrar el gráfico de barras
    plt.show()