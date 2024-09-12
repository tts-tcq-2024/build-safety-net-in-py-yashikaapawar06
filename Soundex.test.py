import unittest
import Soundex  

class TestSoundex(unittest.TestCase):

    def assert_soundex(self, name, expected):
        """Helper function to assert soundex code to avoid repeating logic."""
        self.assertEqual(Soundex.generate_soundex(name), expected)

    def test_empty_string(self):
        cases = [("", "")]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assert_soundex(name, expected)

    def test_characters(self):
        cases = [
            ("A", "A000"),
            ("B", "B000"),
            ("Z", "Z000"),
            ("Aeiou", "A000"),
            ("Hhh", "H000"),
            ("Yy", "Y000")
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assert_soundex(name, expected)

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
                self.assert_soundex(name, expected)

    def assert_process_name(self, name, expected):
        """Helper function to assert process_name output."""
        self.assertEqual(Soundex.process_name(name), expected)

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
                self.assert_process_name(name, expected)

if __name__ == '__main__':
    unittest.main()
