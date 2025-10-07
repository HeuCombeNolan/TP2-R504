#!/usr/bin/python3
import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_base(self):
        self.assertEqual(affiche(), ''.join(['Fizz' if i % 3 == 0 and i % 5 != 0
                                             else 'Buzz' if i % 5 == 0 and i % 3 != 0
                                             else 'FrisBee' if i % 15 == 0
                                             else str(i)
                                             for i in range(1, 101)]))

if __name__ == '__main__':
    unittest.main()

print(affiche())
print(affiche(15))
print(affiche(5, 10))
