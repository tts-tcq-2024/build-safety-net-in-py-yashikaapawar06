SOUNDEX_MAPPING = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}

def get_soundex_code(c):
    return SOUNDEX_MAPPING.get(c.upper(), '0')

def process_char(prev_code, char):
    code = get_soundex_code(char)
    return code if code != '0' and code != prev_code else None

def add_char_to_result(char, prev_code, result):
    code = process_char(prev_code, char)
    if code:
        result.append(code)
        return code
    return prev_code

def process_name(name):
    if not name:
        return ""
    
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    result = [soundex]
    
    for char in name[1:]:
        prev_code = add_char_to_result(char, prev_code, result)

    return ''.join(result)

def generate_soundex(name):
    soundex = process_name(name)
    return soundex[:4].ljust(4, '0') if soundex else ""
