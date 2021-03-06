from Lab05.src.zadanie3 import ChristmasSong
import unittest


class SongTest(unittest.TestCase):

    def test_sigle_vers_one(self):
        self.assertEqual(self.temp.singleVers(1),
                         'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_sigle_vers_seven(self):
        self.assertEqual(self.temp.singleVers(7),
                         'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, ')

    def test_sigle_vers_length_more_than_song_length(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.singleVers(101)

    def test_sigle_vers_not_int(self):
        with self.assertRaisesWithMessage(TypeError):
            self.temp.singleVers("a")

    def test_sigle_vers_minus_vers(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.singleVers(-1)

    def test_section_song_1_2(self):
        self.assertEqual(self.temp.sectionSong(1, 2),
                         ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
                          'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.'])

    def test_section_song_not_int(self):
        with self.assertRaisesWithMessage(TypeError):
            self.temp.sectionSong("a", 4)

    def test_section_song_start_equal_end(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.sectionSong(23, 23)

    def test_section_song_end_more_than_start(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.sectionSong(23, 20)

    def test_section_song_minus_end_and_start(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.sectionSong(-4, -3)

    def test_section_song_length_more_than_song_length(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.sectionSong(100, 120)

    def test_section_all_song_(self):
        self.assertEqual(self.temp.sectionSong(1, len(self.temp.text)), self.temp.text)

    def test_whole_song(self):
        self.assertEqual(self.temp.wholeTextSong(),
                         ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
                          'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a ',
                          'Pear Tree.',
                          'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, ',
                          'and a Partridge in a Pear Tree.',
                          'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, ',
                          'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold ',
                          'Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold ',
                          'Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-',
                          'Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-',
                          'Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a ',
                          'Partridge in a Pear Tree.',
                          'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-',
                          'Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two ',
                          'Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies ',
                          'Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, ',
                          'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                          'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-',
                          'a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, ',
                          'four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'])

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
