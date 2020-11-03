from src.zadanie3 import ChristmasSong
import unittest


class SongTest(unittest.TestCase):

    def test_sigle_vers_one(self):
        self.assertEqual(self.temp.singleVers(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')


    # Utility functions
    def setUp(self):
        self.temp = ChristmasSong()
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
