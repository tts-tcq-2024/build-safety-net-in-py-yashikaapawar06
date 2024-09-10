SOUNDEX_MAPPING = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}
def get_soundex_code(c):
    c = c.upper()
     return SOUNDEX_MAPPING.get(c, '0')

def process_name(name):
    if not name:  # Handle empty string
        return ""

    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    result = [soundex]

    def process_character(char):
        nonlocal prev_code
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            result.append(code)
            prev_code = code

    for char in name[1:]:
        process_char(char)

    return ''.join(result)

def generate_soundex(name):
    if not name:  # Handle empty string
        return ""
    soundex = process_name(name)
    return soundex[:4].ljust(4, '0')
