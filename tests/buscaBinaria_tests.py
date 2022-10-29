import unittest
import sys

from numpy import size
sys.path.append('Conceitos/BuscaBinaria')

from BuscaBinaria import buscaBinaria

class TestBuscaBinaria(unittest.TestCase):
    def test_binarySearch(self):
        arr = [1,3,4,5,7,8,12,92,106]
        self.assertEqual(buscaBinaria(arr, 3), 1)
        self.assertEqual(buscaBinaria(arr, 1), 0)
        self.assertEqual(buscaBinaria(arr, 12), 6)
        self.assertEqual(buscaBinaria(arr, 92), 7)
        self.assertEqual(buscaBinaria(arr, 106), 8)

if __name__ == '__main__':
    unittest.main()