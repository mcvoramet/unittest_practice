# when do the testing use 'python3 -m unittest test_calc.py' on terminal
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):       # make sure name of the function is start with test_...
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):       # make sure name of the function is start with test_...
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):       # make sure name of the function is start with test_...
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):       # make sure name of the function is start with test_...
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        #self.assertRaises(ValueError, calc.divide, 10, 0) # this mean pass in 10 and 0 to divide()

        # use context manager here instead of code above (can use either one)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(calc.power(2, 4), 16)
        self.assertEqual(calc.power(-2, 4), 16)
        self.assertEqual(calc.power(-2, 3), -8)


if __name__ == '__main__':     # if we use this we can just use 'python3 test_calc.py' on terminal to do testing
    unittest.main()
