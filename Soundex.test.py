import unittest
from Soundex import generate_soundex, get_soundex_code, process_name

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_basic_soundex(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Smythe"), "S530")

    def test_repeated_consonants(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_vowels_and_h_w_y(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")

    def test_edge_cases(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("Z"), "Z000")
        self.assertEqual(generate_soundex("Aeiou"), "A000")
        self.assertEqual(generate_soundex("Hhh"), "H000")
        self.assertEqual(generate_soundex("Yy"), "Y000")
    
    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('*'), '0')  # Non-mapped character

    def test_process_name(self):
        self.assertEqual(process_name("Smith"), "S53")
        self.assertEqual(process_name("Ashcraft"), "A261")
        self.assertEqual(process_name("Tymczak"), "T522")
        self.assertEqual(process_name("Robert"), "R163")
        self.assertEqual(process_name("Rupert"), "R163")
        self.assertEqual(process_name("A"), "A")
        self.assertEqual(process_name("B"), "B")
        self.assertEqual(process_name(""), "")

if __name__ == '__main__':
    unittest.main()
