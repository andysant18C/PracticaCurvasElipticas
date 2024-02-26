import random
class Entidad:
    def __init__(self, nombre, mensaje, curva, G, orden_G, llave_privada=None, punto_privado=None):
        self.nombre = nombre
        self.mensaje = mensaje
        self.curva = curva
        self.G = G
        self.orden_G = orden_G
        self.llave_privada = llave_privada if llave_privada is not None else random.randint(1, orden_G)
        if punto_privado is None:
            self.punto_privado = self.curva.mult(self.llave_privada, G)  
        else:
            self.punto_privado = punto_privado
        self.pks= []
        self.llaves_recibidas = []

    def __str__(self):
      return f"Entidad: {self.nombre}, Mensaje: {self.mensaje}, Curva Eliptica: {str(self.curva)}, Punto Generador: {str(self.G)}, Orden de G: {self.orden_G}, Llave Privada: {self.llave_privada}, Punto Privado: {str(self.punto_privado)}, Llaves Publicas: {self.pks}, Llaves Recibidas: {self.llaves_recibidas}"
    def cifrar(self):
        # Aquí va la implementación de cifrado
        pass

    def descifrar(self, parejas_puntos):
        # Aquí va la implementación de descifrado
        pass

    def generaLlavesPublicas(self):
        C_mas_A = self.curva.suma(self.G, self.punto_privado)
        A1 = self.curva.mult(self.llave_privada, C_mas_A)
        A2 = self.curva.mult(self.llave_privada, self.punto_privado)
        self.pks.append(A1)
        self.pks.append(A2)

    def recibeLlavesPublicas(self, pks):
      if isinstance(pks, list) and len(pks) >= 2:
         self.llaves_recibidas.extend(pks)  
      else:
        raise ValueError("Se deben proporcionar un par de llaves públicas.")

    def llavesFinales(self):
      if len(self.llaves_recibidas) == 2:
          Pk2 = self.llaves_recibidas[1]
          Pke = self.curva.mult(self.llave_privada, Pk2)
          self.pks.append(Pke)
          print(f"Llave final de {self.nombre}: {Pke}")
          return self.pks
      else:
        raise ValueError("Error: No se han recibido suficientes llaves públicas para generar la llave final.")
