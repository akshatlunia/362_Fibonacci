import unittest
import pytest
import fibonacci

class testFib(unittest.TestCase):
    def test_Fibonacci(self):
        self.assertEqual(fibonacci.fibonacci(6), 5) #8 because it adds 1 after print
        self.assertEqual(fibonacci.fibonacci(1), 0)
        self.assertEqual(fibonacci.fibonacci(-5), "Invalid Input")

if __name__ == '__main__':
    unittest.main()

def test_Fibonacci_pytest():
    assert fibonacci.fibonacci(6) == 5
    assert fibonacci.fibonacci(1) == 0
    assert fibonacci.fibonacci(-5) == "Invalid Input"
