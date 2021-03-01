import unittest
from keygen import Keygen
import math


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

    def test_modulo_multiplier(self):
        self.assertTrue(math.gcd(self.kg.modulus, self.kg.multiplier) == 1)



if __name__ == '__main__':
    unittest.main()

