import unittest
from StringCalculator import add, NegativeNumberException

class TestStringCalculator(unittest.TestCase):

    def test_expectZeroForEmptyInput(self):
        self.assertEqual(add(""), 0)

    def test_expectZeroForSingleZero(self):
        self.assertEqual(add("0"), 0)

    def test_expectSumForTwoNumbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_ignoreNumbersGreaterThan1000(self):
        self.assertEqual(add("1,1001"), 1)

    def test_expectSumWithCustomDelimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_expectSumWithNewlineDelimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_negativeNumberThrowsException(self):
        with self.assertRaises(NegativeNumberException) as context:
            add("1,-2,3")
        self.assertIn("-2", str(context.exception))

    def test_multipleNegativesThrowsException(self):
        with self.assertRaises(NegativeNumberException) as context:
            add("1,-2,-3")
        self.assertIn("Negatives not allowed: -2, -3", str(context.exception))

    def test_expectSumWithLargeCustomDelimiter(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_expectSumWithMultipleDelimiters(self):
        self.assertEqual(add("1\n2,3"), 6)

if __name__ == "__main__":
    unittest.main()
