class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def equals(self, otro_punto):
        return self.x == otro_punto.x and self.y == otro_punto.y

    def set(self, x, y):
        self.x = x
        self.y = y
