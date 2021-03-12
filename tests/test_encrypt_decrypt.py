import unittest
import encrypt_decrypt

class MyTestCase(unittest.TestCase):
    def test__to_binary(self):
        as_binary = encrypt_decrypt._to_binary(".бb")
        test = True
        for binary in as_binary:
            if len(binary) != 8:
                test = False
                break
        print(as_binary)
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()
