def main():
    # Crear una curva elíptica y un punto generador
    curva = CurvaEliptica(a, b, p)
    G = Punto(x, y)

    # Crear dos entidades
    entidad1 = Entidad("Entidad 1", "Hola, Entidad 2", curva, G, orden_G, tabla)
    entidad2 = Entidad("Entidad 2", "Hola, Entidad 1", curva, G, orden_G, tabla)

    # Generar y compartir llaves públicas
    llaves_publicas1 = entidad1.generaLlavesPublicas()
    llaves_publicas2 = entidad2.generaLlavesPublicas()
    entidad1.recibeLlavesPublicas(llaves_publicas2)
    entidad2.recibeLlavesPublicas(llaves_publicas1)

    # Cifrar y descifrar mensajes
    mensaje_cifrado1 = entidad1.cifrar()
    mensaje_cifrado2 = entidad2.cifrar()
    mensaje_descifrado1 = entidad2.descifrar(mensaje_cifrado1)
    mensaje_descifrado2 = entidad1.descifrar(mensaje_cifrado2)

    # Imprimir los mensajes descifrados
    print(f"{entidad2.nombre} descifró el mensaje: {mensaje_descifrado1}")
    print(f"{entidad1.nombre} descifró el mensaje: {mensaje_descifrado2}")

if __name__ == "__main__":
    main()
""""
se debe remplazar a, b, p, x, y, 
orden_G y tabla con los valores que se esten  utilizando para la curva elíptica y el punto generador.
 se debe  implementar los métodos cifrar y descifrar en la clase Entidad para que este 
 código funcione correctamente
"""
