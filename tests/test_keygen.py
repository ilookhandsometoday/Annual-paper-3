import unittest
import math
from keygen import Keygen


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.kg = Keygen()

    def test_sequence_generation(self):
        sum = 0
        test = True
        for element in self.kg.seq:
            if element < sum:
                test = False
                break
            sum += element
        self.assertTrue(test)

    def test_modulo(self):
        self.assertTrue(self.kg.modulus > sum(self.kg.seq))

    def test_modulo_multiplier(self):
        self.assertTrue(math.gcd(self.kg.modulus, self.kg.multiplier) == 1)

    def test_multiplier_mod_inverse(self):
        self.assertEqual(self.kg.multiplier*self.kg.multiplier_mod_inverse % self.kg.modulus, 1)



if __name__ == '__main__':
    unittest.main()

