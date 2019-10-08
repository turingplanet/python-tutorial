import unittest 
from mydict import MyDict

class TestDict(unittest.TestCase):
    def setUp(self): 
        self.keys = {'a', 'b', 'c', 'd'}
        self.values = {'1', '2', '3', '4'}
        self.dict = MyDict()
    
    def testDict(self):
        for i in range(0, len(self.keys)):
            self.dict.put(self.keys.pop(), self.values.pop())
        for i in range(0, len(self.keys)):
            self.assertEqual(self.dict.get[self.keys[i]], self.values[i])

if __name__ == '__main__':     
    unittest.main()