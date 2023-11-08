import unittest

class ATester(unittest.TestCase):
    def test_div_par_zero_pas_ok(self):
        with self.assertRaises(Exception):
            c=2/0

    def test_b(self):
        a=1
        b=2
        c=a/b
        self.assertEquals(0.5,c)
