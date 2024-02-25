import random

class Entidad:
    def __init__(self, nombre, mensaje, curva, G, orden_G, tabla):
        self.nombre = nombre
        self.mensaje = mensaje
        self.curva = curva
        self.G = G
        self.orden_G = orden_G
        self.llave_privada = random.randint(1, orden_G)
        self.punto_privado = random.choice(curva.puntos())
        self.llaves_publicas = []
        self.llaves_recibidas = []
        self.tabla = tabla

    def __str__(self):
        return f"Entidad: {self.nombre}, Mensaje: {self.mensaje}, Curva Eliptica: {str(self.curva)}, Punto Generador: {str(self.G)}, Orden de G: {self.orden_G}, Llave Privada: {self.llave_privada}, Punto Privado: {str(self.punto_privado)}, Llaves Publicas: {self.llaves_publicas}, Llaves Recibidas: {self.llaves_recibidas}"

    def cifrar(self):
        # Aquí va la implementación de cifrado
        pass

    def descifrar(self, parejas_puntos):
        # Aquí va la implementación de descifrado
        pass

    def generaLlavesPublicas(self):
        # Aquí va la implementación de generación de llaves públicas
        pass

    def recibeLlavesPublicas(self, pks):
        # Aquí va la implementación de recepción de llaves públicas
        pass

    def llavesFinales(self):
        # Aquí va la implementación de generación de llaves finales
        pass
