import unittest
import sys


sys.path.append('Estrutura_de_Dados/listaEncadeada')

from listaEncadeada import ListaEncadeada

class TestListaEncadeada(unittest.TestCase):
    def test_append(self):
        listTest = ListaEncadeada()
        listTest.append(5)
        listTest.append(8)
        listTest.append(10)
        self.assertEqual(str(listTest), '[5 -> 8 -> 10 -> None]')

    def test_deleteWithValue(self):
        listTest = ListaEncadeada()
        listTest.append(5)
        listTest.append(8)
        listTest.append(10)
        self.assertEqual(str(listTest), '[5 -> 8 -> 10 -> None]')
        listTest.deleteWithValue(8)
        self.assertEqual(str(listTest), '[5 -> 10 -> None]')
        listTest.deleteWithValue(15)
        self.assertEqual(str(listTest), '[5 -> 10 -> None]')
        listTest.deleteWithValue(5)
        self.assertEqual(str(listTest), '[10 -> None]')

if __name__ == '__main__':
    unittest.main()