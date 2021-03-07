import unittest
import p1_fizzbuzz

class FizzBuzzTest(unittest.TestCase):
  def test_fizzBuzz1(self):
    self.assertEqual(self.test_case(), p1_fizzbuzz.output(1, 35))

  def test_case(self):
    return '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34'

if __name__ == '__main__':
    unittest.main()