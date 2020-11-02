from src.zadanie1 import Hamming
import unittest


class HammingTest(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(self.temp.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(self.temp.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(self.temp.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(self.temp.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(self.temp.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("ATA", "AGTG")


    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("", "G")

   
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("G", "")

    # Utility functions
    def setUp(self):
        self.temp = Hamming()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
