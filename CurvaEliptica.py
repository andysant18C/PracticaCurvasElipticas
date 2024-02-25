import Punto;
class CurvaEliptica:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.infinito = Punto(None, None)

    def __str__(self):
        return f"Curva Eliptica: y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})"

    def tiene(self, punto):
        return (punto.y ** 2) % self.p == (punto.x ** 3 + self.a * punto.x + self.b) % self.p

    def puntos(self):
        puntos = [self.infinito]
        for x in range(self.p):
            for y in range(self.p):
                punto = Punto(x, y)
                if self.tiene(punto):
                    puntos.append(punto)
        return puntos

    def orden(self, punto):
        k = 1
        while True:
            resultado = self.mult(k, punto)
            if resultado == self.infinito:
                return k
            k += 1

    def cofactor(self, punto):
        return len(self.puntos()) // self.orden(punto)

    def suma(self, p, q):
        if p == self.infinito:
            return q
        if q == self.infinito:
            return p
        if p.x == q.x and (p.y != q.y or p.y == 0):
            return self.infinito
        if p != q:
            lam = ((q.y - p.y) * pow(q.x - p.x, self.p - 2, self.p)) % self.p
        else:
            lam = ((3 * p.x ** 2 + self.a) * pow(2 * p.y, self.p - 2, self.p)) % self.p
        x3 = (lam ** 2 - p.x - q.x) % self.p
        y3 = (lam * (p.x - x3) - p.y) % self.p
        return Punto(x3, y3)

    def mult(self, k, punto):
        resultado = self.infinito
        addend = punto
        while k:
            if k & 1:
                resultado = self.suma(resultado, addend)
            addend = self.suma(addend, addend)
            k >>= 1
        return resultado

    def inv(self, punto):
        return Punto(punto.x, -punto.y % self.p)
