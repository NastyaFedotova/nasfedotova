from main import *
import unittest

class TestQr(unittest.TestCase):
    def setUp(self):
        self.get_coef = get_coef
        self.get_roots = get_roots
    def test_roots(self):
        self.assertTrue(len(self.get_roots(0, 0, 0)) > 4)
        self.assertEqual(self.get_roots(-1, -1, -1), [])
        self.assertEqual(self.get_roots(1, 1, 1), [])
        self.assertEqual(self.get_roots(1, 0, 0), [0,])
        self.assertEqual(self.get_roots(0, 0, 1), [])
        self.assertEqual(self.get_roots(0, 1, 0), [0,])
        self.assertEqual(self.get_roots(0, 1, 1), [])
        self.assertEqual(self.get_roots(1, 0, 1), [])
        self.assertEqual(self.get_roots(20, 100, 0), [0,])

        self.assertEqual(set(self.get_roots(1, -6, 5)), set([-5 ** 0.5, -1, 1, 5 ** 0.5]))
        self.assertEqual(set(self.get_roots(1, -2, -8)), set([-2, 2]))
        self.assertEqual(set(self.get_roots(1, -8, -9)), set([-3, 3]))
        self.assertEqual(set(self.get_roots(1, -7, 6)), set([-1, 1, -6 ** 0.5, 6 ** 0.5]))
        self.assertEqual(set(self.get_roots(1, 5, 9)), set([]))
        self.assertEqual(set(self.get_roots(1, -13, 0)), set([-13 ** 0.5, 0, 13 ** 0.5]))
        self.assertEqual(set(self.get_roots(1, -17, 16)), set([-4, -1, 1, 4]))


if __name__ == '__main__':
    unittest.main()
