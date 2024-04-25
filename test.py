import unittest
from main_file import utils

class TestAdd(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(utils.add(1, 2), 3)

class TestSub(unittest.TestCase):
    def test_sub_function(self):
        self.assertEqual(utils.sub(55, 5), 50)

class TestMul(unittest.TestCase):
    def test_mul_function(self):
        self.assertEqual(utils.mul(1, 2), 2)

class TestDiv(unittest.TestCase):
    def test_div_function(self):
        self.assertEqual(utils.div(10, 5), 2)

class TestMod(unittest.TestCase):
    def test_mod_function(self):
        self.assertEqual(utils.mod(100, 2), 0)

class TestLcm(unittest.TestCase):
    def test_lcm_function(self):
        self.assertEqual(utils.lcm(54, 24), 216)

class TestHcf(unittest.TestCase):
    def test_hcf_function(self):
        self.assertEqual(utils.hcf(54, 24), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)