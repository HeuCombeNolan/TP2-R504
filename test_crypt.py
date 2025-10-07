#!/usr/bin/python3
import unittest
from cryptage import crypt, decrypt

class TestCryptage(unittest.TestCase):
    def test_crypt_base(self):
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_pas(self):
        self.assertEqual(crypt("abc", 2), "cde2")

    def test_decrypt(self):
        msg = crypt("hello!", 3)
        self.assertEqual(decrypt(msg), "hello!")

if __name__ == '__main__':
    unittest.main()
