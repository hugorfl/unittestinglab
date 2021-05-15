"""
Test Cases:
1 [TTP] Identical files compared
2 [TTF] Non equal files compared
3 [TTF] Non existing file compared to an existing one
4 [TTF] Passing None
"""


from filecmp import cmp
import unittest


class FileCmpTest(unittest.TestCase):
    def test_pass_identical_files_compared(self):
        self.assertTrue(cmp('./lorem-ipsum2.txt', './lorem-ipsum3.txt', False))

    def test_fail_non_equal_files_compared(self):
        self.assertFalse(cmp('./lorem-ipsum.txt', './lorem-ipsum2.txt', False))

    def test_fail_non_existing_file_compared_to_existing(self):
        with self.assertRaises(FileNotFoundError):
            cmp('./corporate-ipsum.txt', './lorem-ipsum.txt', False)

    def test_fail_none_passed(self):
        with self.assertRaises(TypeError):
            cmp(None, None, False)


if __name__ == '__main__':
    unittest.main()
