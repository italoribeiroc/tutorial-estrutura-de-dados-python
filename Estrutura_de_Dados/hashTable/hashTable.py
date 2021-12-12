import sys
sys.path.append('Estrutura_de_Dados/listaEncadeada')

from listaEncadeada import ListaEncadeada

class HashTable:
    def __init__(self, size = 10) -> None:
        self.data = [ListaEncadeada() for i in range(size)]
        self.size = size

    def getHashCode(self, key):
        return sum([ord(char) for char in key])

    def convertToIndex(self, hashCode):
        return hashCode % self.size
    
    def put(self, key, value):
        hashCode = self.getHashCode(key)
        index = self.convertToIndex(hashCode)
        self.data[index].append((key, value))

    def get(self, key):
        hashCode = self.getHashCode(key)
        index = self.convertToIndex(hashCode)
        current = self.data[index].head
        while current != None:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
