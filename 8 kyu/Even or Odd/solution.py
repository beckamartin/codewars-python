import unittest


def even_or_odd(number):
    if number % 2 == 0: return "Even"
    else: return "Odd"


class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd(2), "Even")

    def test_odd(self):
        self.assertEqual(even_or_odd(3), "Odd")

        
if __name__ == '__main__':
    unittest.main()