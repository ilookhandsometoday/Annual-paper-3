import unittest
from keygen import Keygen
import math


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.kg = Keygen()

    def test_find_modulus(self):
        print("_find_modulus")
        print(self.kg.modulus)
        print(sum(self.kg.seq))
        self.assertTrue(self.kg.modulus > sum(self.kg.seq))

    def test_find_multiplier(self):
        print("_find_multiplier")
        print(self.kg.modulus)
        print(self.kg.multiplier)
        self.assertTrue(math.gcd(self.kg.modulus, self.kg.multiplier) == 1 and self.kg.modulus > self.kg.multiplier > 1)

    def test_generate_si_sequence(self):
        seq = Keygen.generate_si_sequence()
        seq_sum = 0
        test = True
        for element in seq:
            if element <= seq_sum:
                test = False
                break
            seq_sum += element
        print("generate_si_sequence")
        print(seq)
        print(sum(seq))
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()

