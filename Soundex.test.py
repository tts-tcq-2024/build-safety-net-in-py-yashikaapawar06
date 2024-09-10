import unittest
from Soundex import generate_soundex, process_name, get_soundex_code

class TestSoundex(unittest.TestCase):

    def test_empty_and_single_characters(self):
        cases = [
            ("", ""),
            ("A", "A000"),
            ("B", "B000"),
            ("Z", "Z000"),
            ("Aeiou", "A000"),
            ("Hhh", "H000"),
            ("Yy", "Y000")
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(generate_soundex(name), expected)

    def test_soundex(self):
        cases = [
            ("Smith", "S530"),
            ("Smythe", "S530"),
            ("Pfister", "P236"),
            ("Robert", "R163"),
            ("Rupert", "R163")
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(generate_soundex(name), expected)


    def test_process_name(self):
        cases = [
            ("Smith", "S53"),
            ("Robert", "R163"),
            ("Rupert", "R163"),
            ("A", "A"),
            ("B", "B"),
            ("", "")
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(process_name(name), expected)

if __name__ == '__main__':
    unittest.main()
