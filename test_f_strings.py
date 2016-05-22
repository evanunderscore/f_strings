import datetime
import decimal
import unittest

from f_strings import f


class TestFStrings(unittest.TestCase):
    def test_fred(self):
        name = 'Fred'
        age = 50
        anniversary = datetime.date(1991, 10, 12)
        self.assertEqual(
            f('My name is {name}, my age next year is {age+1}, '
              'my anniversary is {anniversary:%A, %B %d, %Y}.'),
            'My name is Fred, my age next year is 51, '
            'my anniversary is Saturday, October 12, 1991.')
        self.assertEqual(
            f('He said his name is {name!r}.'),
            "He said his name is 'Fred'.")

    def test_decimal(self):
        width = 10
        precision = 4
        value = decimal.Decimal('12.34567')
        self.assertEqual(
            f('result: {value:{width}.{precision}}'),
            'result:      12.35')

    def test_empty(self):
        with self.assertRaises(ValueError):
            f('{}')
        with self.assertRaises(ValueError):
            f('{ }')
