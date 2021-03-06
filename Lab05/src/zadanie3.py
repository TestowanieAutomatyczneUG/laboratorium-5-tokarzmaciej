class ChristmasSong:
    def __init__(self):
        self.text = ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
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
                     'four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.']

    def singleVers(self, number):
        if type(number) != int:
            raise TypeError('number have to be int')
        if len(self.text) < number:
            raise ValueError('not have this verse in the song')
        if 0 >= number:
            raise ValueError('minus number')
        else:
            return self.text[number - 1]

    def sectionSong(self, start, end):
        if type(start) != int or type(end) != int:
            raise TypeError('start and end have to be int')
        if start == end:
            raise ValueError('start can not equal end')
        if start > end:
            raise ValueError('end have to more than start')
        if start <= 0 or end <= 0:
            raise ValueError('start and end have to more zero')
        if start > len(self.text) or end > len(self.text):
            raise ValueError('start and end have to less than song length')
        return self.text[start - 1:end]

    def wholeTextSong(self):
        return self.text
