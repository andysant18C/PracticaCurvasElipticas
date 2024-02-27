from CurvaEliptica import CurvaEliptica
from Entidad import Entidad
from Punto import Punto

# Tabla de caracteres
tabla = {
    '*': Punto.infinite_point,  # Punto al infinito 
    'a': Punto(5, 25),
    'b': Punto(1, 30),
    'c': Punto(21, 32),
    'd': Punto(7, 25),
    'e': Punto(25, 12),
    'f': Punto(4, 28),
    'g': Punto(0, 34),
    'h': Punto(16, 17),
    'i': Punto(15, 26),
    'j': Punto(27, 32),
    'k': Punto(9, 4),
    'l': Punto(2, 24),
    'm': Punto(26, 5),
    'n': Punto(33, 14),
    'o': Punto(11, 17),
    'p': Punto(31, 22),
    'q': Punto(13, 30),
    'r': Punto(35, 21),
    's': Punto(23, 7),
    't': Punto(10, 17),
    'u': Punto(29, 6),
    'v': Punto(29, 31),
    'w': Punto(10, 20),
    'x': Punto(23, 30),
    'y': Punto(35, 16),
    'z': Punto(13, 7),
    '1': Punto(31, 15),
    '2': Punto(11, 20),
    '3': Punto(33, 23),
    '4': Punto(26, 32),
    '5': Punto(2, 13),
    '6': Punto(9, 33),
    '7': Punto(27, 5),
    '8': Punto(15, 11),
    '9': Punto(16, 20),
    '0': Punto(0, 3),
    '#': Punto(4, 9),
    '@': Punto(25, 25),
    '!': Punto(7, 12),
    '&': Punto(21, 5),
    '$': Punto(1, 7),
    '%': Punto(5, 12)
}

def prueba_curva():
    # parametros
    a = 2
    b = 2
    p = 17
    G = Punto(5, 1)
    curva = CurvaEliptica(a, b, p)

    print("k | kG | kG en EC?")
    print("------------------")
    for k in range(1, 20):
        kG = curva.mult(k, G)
        on_curve = curva.tiene(kG)
        print(f"{k} | {kG} | {on_curve}")
    print(f"\norden(G) = {curva.orden(G)}")
    print(f"cofactor(G) = {curva.cofactor(G)}")
    

def main():
    # Curva y punto G
    curva = CurvaEliptica(2, 9, 37)
    G = Punto(9, 4)
    # Puntos fijos de ejemplo
    punto_allice = Punto(10,20)
    punto_bob = Punto(11,20)

    # Creamos a Allice y Bob
    allice = Entidad("Allice", "Mensaje secreto de Allice", curva, G, curva.orden(G),5,punto_allice)
    bob = Entidad("Bob", "Mensaje secreto de Bob", curva, G, curva.orden(G),7,punto_bob)

    # Generamos y compartir llaves publicas de Allice y Bob
    allice.generaLlavesPublicas()
    #print(f"\nLlaves publicas de Allice {allice.pks}")
    bob.generaLlavesPublicas()
    #print(f"\nLlaves publicas de Bob {bob.pks}")
    # Allice recibe las llaves publicas de Bob
    allice.recibeLlavesPublicas(bob.pks)
    #print(f"\nAllice recibe las llaves de BOB y son: {allice.llaves_recibidas}")
    bob.recibeLlavesPublicas(allice.pks)
    #print(f"\nBob recibe las llaves de Allice y son: {bob.llaves_recibidas}")

    allice.llavesFinales()
    #print(f"\nLlaves finales de Allice {allice.pks}")
    #print("\nLlaves Publicas de Allice:", allice.pks)
    bob.llavesFinales()
    #print(f"\nLlaves finales de Bob{bob.pks}")
    # Intercambiamos la última clave de cada uno
    #allice.pks[2], bob.pks[2] = bob.pks[2] ,allice.pks[2] 
    # Allice recibe la ultima llave de Bob
    allice.llaves_recibidas.append(bob.pks[2])
    #allice.recibeLlavesPublicas(bob.pks)
    # Bob recibe la ultima llave de Allice
    bob.llaves_recibidas.append(allice.pks[2])
    print("\nLlaves Públicas FINALES de Allice:", allice.pks)
    print("\n Llaves recibidas de allice: ",allice.llaves_recibidas)
    print("\nLlaves Públicas FINALES de BOB:", bob.pks)
    print("\n Llaves recibidas de bob: ",bob.llaves_recibidas)
    # Bob cifra el mensaje 'Attack'
    mensaje_cifrado_bob = bob.cifrar('attack',tabla)
    print(f"Mensaje cifrado por BOB: {mensaje_cifrado_bob}")
    
    
if __name__ == "__main__":
    main()
