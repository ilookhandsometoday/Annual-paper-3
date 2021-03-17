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

    def test__chunk_text_(self):
        self.assertEqual(list(encrypt_decrypt._chunk_text("12345678", 4)), ["1234", "5678"])

    def test__restore_chunk(self):
        self.assertEqual(encrypt_decrypt._restore_chunk([3, 4, 5, 1, 20]), "010111000000000000001" + 79*"0")

if __name__ == '__main__':
    unittest.main()
