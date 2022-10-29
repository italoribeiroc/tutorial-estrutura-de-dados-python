import unittest
import sys

from numpy import size
sys.path.append('Estrutura_de_Dados/hashTable')

from hashTable import HashTable

class TestHashTable(unittest.TestCase):
    def test_hashCode(self):
        hashTest = HashTable()
        self.assertEqual(hashTest.getHashCode(key = 'aB'), ord('a') + ord('B'))

    def test_get(self):
        hashTest = HashTable()
        hashTest.put('teste', 1)
        hashTest.put('teste', 2)
        self.assertEqual(hashTest.get('teste'), 2)
        hashTest.put('teste', 1)
        self.assertEqual(hashTest.get('teste'), 1)

    def test_put(self):
        hashTest = HashTable()
        hashTest.put('teste1', 5)
        self.assertEqual(hashTest.get('teste1'), 5)
        self.assertEqual(hashTest.get('teste2'), None)

    def test_convertToIndex(self):
        hashTest = HashTable(size = 8)
        self.assertEqual(hashTest.convertToIndex(8), 0)
        self.assertEqual(hashTest.convertToIndex(21), 5)

if __name__ == '__main__':
    unittest.main()