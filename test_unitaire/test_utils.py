# import unittest classe pour les methodes suivant
# assertEqual(a, b)             a == b                      "a" égale à "b"
# assertNotEqual(a, b)          a != b                      "a" n'est pas égale à "b"
# assertTrue(x)                 bool(x) is True             le boolean est à True
# assertFalse(x)                bool(x) is False            le boolean est à False
# assertIs(a, b)                a is b                      "a" est "b"
# assertIsNot(a, b)             a is not b                  "a" n'est pas "b"
# assertIsNone(x)               x is  None                  "x" est null
# assertIsNotNone(x)            x is not None               "x" n'est pas null
# assertIn(a, b)                a in b                      il y a "a" dans "b"
# assertNotIn(a, b)             a not in b                  il n'y a pas "a" dans "b"
# assertIsInstance(a, b)        is intace (a, b)            il y a "a" dans "b"
# assertNotIsInstance(a, b)     not is instance(a, b)       il n'y a pas "a" dans "b"

import unittest
import utils

class TestUtils(unittest.TestCase):
    #lancement des méthodes

    def test_is_prime(self):
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))

    def test_cubic(self):
        self.assertEqual(utils.cubic(2), 8)
        self.assertEqual(utils.cubic(-2), -8)
        self.assertNotEqual(utils.cubic(2), 4)
        self.assertNotEqual(utils.cubic(-3), 27)

    def test_say_hello(self):
        self.assertEqual(utils.say_hello("lucas"), "Hello, lucas")
        self.assertEqual(utils.say_hello("eden"), "Hello, eden")
        self.assertNotEqual(utils.say_hello("lucas"), "Hi, lucas")
        self.assertNotEqual(utils.say_hello("eden"), "Hi, eden")

    def test_somme(self):
        self.assertEqual(utils.somme(1), 9)
        self.assertNotEqual(utils.somme(1), 1)


#lancement des tests
if __name__ == '__main__':
    unittest.main()