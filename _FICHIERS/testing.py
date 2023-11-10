import unittest
from fonctions import *

class ATester(unittest.TestCase):

    def setUp(self) -> None:
        self.data = range(1,10000000)

    def test_data_contient_1_et_2(self):
        self.assertIn(1, self.data)
        self.assertIn(2, self.data)

    def test_div_par_zero_pas_ok(self):

        with self.assertRaises(Exception):
            c=2/2

    def test_b(self):
        a=1
        b=2
        c=a/b
        self.assertEquals(0.5,c)

    def test_c(self):
        self.assertTrue(1==1)

    def test_transfert_de_1000_OK(self):
        res = transfert(1,2,1000)

        self.assertTrue(res)

    def test_transfert_de_100000000_KO(self):
        res = transfert(1, 2, 100000000)

        self.assertFalse(res)
        self.assertEquals(False, res)
        self.assertIn(2, [1,2,3])

