class Fila:
    def __init__(self):
        self.fila = []

    def pop(self):
        self.fila.pop()

    def push(self, valor):
        self.fila.insert(0,valor)
