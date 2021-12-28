import config
from config import get_path
import unittest
import os

cur_path = os.path.dirname(os.path.abspath(__file__))

class TestBot(unittest.TestCase):
    def test_1(self):
        w = get_path("1", "1", "0")
        self.assertEqual(w, cur_path+"/img/110.jpg")
    def test_2(self):
        w = get_path("0", "1", "0")
        self.assertEqual(w, cur_path + "/img/010.jpg")
    def test_3(self):
        w = get_path("2", "1", "2")
        self.assertEqual(w, cur_path + "/img/212.jpg")

if __name__ == '__main__':
    unittest.main() 
