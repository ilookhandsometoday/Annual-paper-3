import unittest
import encrypt_decrypt

class MyTestCase(unittest.TestCase):
    def test__to_binary_leading_zeros(self):
        as_binary = encrypt_decrypt._to_binary(".бb")
        test = True
        for binary in as_binary:
            if len(binary) != 8:
                test = False
                break
        print(as_binary)
        self.assertTrue(test)

    def test__to_binary(self):
        as_binary = encrypt_decrypt._to_binary("cd")
        self.assertEqual(as_binary, ["01100011", "01100100"])


if __name__ == '__main__':
    unittest.main()
