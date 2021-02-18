import unittest
from keygen import Keygen


class MyTestCase(unittest.TestCase):

    def test_generate_si_sequence(self):
        seq = self.keygen.generate_si_sequence()
        seq_sum = 0
        test = True
        for element in seq:
            if element <= seq_sum:
                test = False
                break
            seq_sum += element
        print(seq)
        self.assertTrue(test, seq)

    def setUp(self):
        self.keygen = Keygen()


if __name__ == '__main__':
    unittest.main()

