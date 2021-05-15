"""
Test Cases:

1 [TTP] Same zero and positive integer is returned
2 [TTP] Same negative integer is returned
3 [TTP] Zero and positive floats with several decimals rounds up
4 [TTP] Negative decimal floats with several decimals rounds up
5 [TTF] Passing stringified zero and positive float number
6 [TTF] Passing stringified negative float number
7 [TTF] Passing other data types other than ints and floats
8 [TTF] Passing None
"""


from math import ceil
import unittest


class CeilTest(unittest.TestCase):
    def test_pass_same_passed_zero_n_positive_int_is_returned(self):
        self.assertEqual(0, ceil(0))
        self.assertEqual(4, ceil(4))
        self.assertEqual(2048, ceil(2048))
        self.assertEqual(9876543210, ceil(9876543210))

    def test_pass_same_negative_int_is_returned(self):
        self.assertEqual(-4, ceil(-4))
        self.assertEqual(-2048, ceil(-2048))
        self.assertEqual(-9876543210, ceil(-9876543210))

    def test_pass_zero_n_positive_floats_with_many_decimals_rounds_up(self):
        self.assertEqual(1, ceil(0.000000000001))
        self.assertEqual(2, ceil(1.00000009))
        self.assertEqual(4, ceil(3.709))
        self.assertEqual(178, ceil(177.9876543210))
        self.assertEqual(5, ceil(4.55))
        self.assertEqual(9876543211, ceil(9876543210.9876543210))

    def test_pass_negative_floats_with_several_decimals_passed_rounds_up(self):
        self.assertEqual(0, ceil(-0.000000000009))
        self.assertEqual(-3, ceil(-3.709))
        self.assertEqual(-256, ceil(-256.9876543210))
        self.assertEqual(-4, ceil(-4.55))
        self.assertEqual(-9876543210, ceil(-9876543210.9876543210))

    def test_fail_stringified_zero_and_positive_float_numbers_passed(self):
        with self.assertRaises(TypeError):
            ceil("0")

        with self.assertRaises(TypeError):
            ceil("14.5")

        with self.assertRaises(TypeError):
            ceil("9876543210.9876543210")

    def test_fail_stringified_negative_float_numbers_passed(self):
        with self.assertRaises(TypeError):
            ceil("-14.5")

        with self.assertRaises(TypeError):
            ceil("-9876543210.9876543210")

    def test_fail_other_types_than_ints_or_floats_passed(self):
        with self.assertRaises(TypeError):
            ceil(-14.5 + 9j)

        with self.assertRaises(TypeError):
            ceil([14.5])

        with self.assertRaises(TypeError):
            ceil((14.5,))

        with self.assertRaises(TypeError):
            ceil({14.5: 14.5})

    def test_fail_none_passed(self):
        with self.assertRaises(TypeError):
            ceil(None)


if __name__ == '__main__':
    unittest.main()
