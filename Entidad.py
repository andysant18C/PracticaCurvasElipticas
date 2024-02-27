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
  
    def cifrar(self, mensaje, tabla):
        #print(f"CIFRADO DE MENSAJE {mensaje}")
        mensaje_cifrado = []
        #random_n = [8,12,19,2,3,23] Se usa para probar el ejemplo
        #cont = 0
        for caracter in mensaje:
            #r = random_n[cont] Se usa para probar el ejemplo
            #cont+=1
            r = random.randint(1, self.orden_G)
            #print(f"{caracter} cifrado como:")
            #print(f"rand = {r}")

            # e1 = r(C)
            e1 = self.curva.mult(r, self.G)
            caracter_e1 =self.obtener_caracter(tabla,e1) 
            
            #print(f"{caracter} {e1}  {caracter_e1}\n", end="")
            # e2 = M + (β + r)A1 − r(A2) + Ae
            M = tabla[caracter]
            beta_r_A1 = self.curva.mult(self.llave_privada+r, self.llaves_recibidas[0])
            r_A2 = self.curva.mult(r, self.llaves_recibidas[1])
            e2 = self.curva.suma(M, beta_r_A1)
            e2 = self.curva.resta(e2,r_A2)
            e2 = self.curva.suma(e2,self.llaves_recibidas[2])
            caracter_e2 = self.obtener_caracter(tabla,e2) 
            #print(f"{caracter} {e2}  {caracter_e2}\n", end="")

            # Agregar los puntos (e1, e2) al mensaje cifrado
            mensaje_cifrado.append((caracter_e1, caracter_e2))

        #print(f"Mensaje cifrado: {mensaje_cifrado}")
        return mensaje_cifrado

    def descifrar(self, parejas_puntos):
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

    def obtener_caracter(self, diccionario, punto):
        for key, value in diccionario.items():
            if value == punto:
                return key
        return None