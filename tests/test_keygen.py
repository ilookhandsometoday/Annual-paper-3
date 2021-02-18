import unittest
from keygen import Keygen
import math


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.kg = Keygen()

    def test_find_q(self):
        print(self.kg.q)
        print(sum(self.kg.w))
        self.assertTrue(self.kg.q > sum(self.kg.w))

    def test_find_r(self):
        print(self.kg.q)
        print(self.kg.r)
        self.assertTrue(math.gcd(self.kg.q, self.kg.r) == 1 and self.kg.q > self.kg.r > 1)

    def test_generate_si_sequence(self):
        seq = Keygen.generate_si_sequence(128)  # 128 because that's the size of chunks
        seq_sum = 0
        test = True
        for element in seq:
            if element <= seq_sum:
                test = False
                break
            seq_sum += element
        print(seq)
        print(sum(seq))
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()

