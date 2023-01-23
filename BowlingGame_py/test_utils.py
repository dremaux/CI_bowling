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
import bowling

class TestUtils(unittest.TestCase):
    
    def test_bowling_score(self):
        self.assertEqual(bowling.bowlingScore('00 34 4/ 13 02 54 16 10 81 XXX'), 80)
        
    def test_perfect_game(self):
        self.assertEqual(bowling.bowlingScore('X X X X X X X X X XXX'), 300)
    
    def test_noob_game(self):
        self.assertEqual(bowling.bowlingScore('00 00 00 00 00 00 00 00 00 00'), 0)
    
    def test_not_equal_game(self):  
        self.assertNotEqual(bowling.bowlingScore('00 34 4/ 13 02 54 16 10 81 XXX'), 516000)
        

    def test_check_value(self):
        # exemple de resumé d'une partie
        frames = '00 34 4/ 13 02 54 16 10 81 XXX'
        frame = frames.split(" ")
        
        self.assertEqual(bowling.checkValue(frame[9][1]), 10)
        self.assertEqual(bowling.checkValue(frame[2][0]), 4)
        self.assertEqual(bowling.checkValue(frame[3][0]), 1)
        self.assertEqual(bowling.checkValue(frame[2][1]), "/")
        
        
    def test_not_check_value(self):
        # exemple de resumé d'une partie
        frames = '00 34 4/ 13 02 54 16 10 81 XXX'
        frame = frames.split(" ")
        
        self.assertNotEqual(bowling.checkValue(frame[4][0]), "/")
        self.assertNotEqual(bowling.checkValue(frame[7][1]), 10)
        
        
    def test_error_check_value(self):
        # exemple de resumé d'une partie
        frames = '00 34 4/ 13 02 54 16 10 81 XXX'
        frame = frames.split(" ")
        
        self.assertEqual(bowling.checkValue(3000), "error")
        self.assertEqual(bowling.checkValue(10), "error")
        self.assertEqual(bowling.checkValue(-1), "error")
        
        
        
    def test_add_spare(self):
        # exemple de resumé d'une partie
        frames = '61 90 4/ 25 02 5/ 16 10 8/ 01'
        frame = frames.split(" ")
        
        self.assertEqual(bowling.addSpare(frame[2][0]), 6)
        self.assertEqual(bowling.addSpare(frame[5][0]), 5)
        self.assertEqual(bowling.addSpare(frame[8][0]), 2)
        

    def test_not_add_spare(self):
        # exemple de resumé d'une partie
        frames = '61 90 4/ 25 02 5/ 16 10 8/ 01'
        frame = frames.split(" ")
        
        self.assertNotEqual(bowling.addSpare(frame[4][0]), 8)
        self.assertNotEqual(bowling.addSpare(frame[7][0]), 6)
        
    
    def test_error_add_spare(self):
        # exemple de resumé d'une partie
        frames = '00 34 4/ 13 02 54 16 10 81 XXX'
        frame = frames.split(" ")
        
        self.assertEqual(bowling.addSpare(3000), "error")
        self.assertEqual(bowling.addSpare(11), "error")
        self.assertEqual(bowling.addSpare(-1), "error")
        
        
    
#lancement des tests
if __name__ == '__main__':
    unittest.main()