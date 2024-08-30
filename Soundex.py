def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def process_name(name):
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    result = [soundex]

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != prev_code and code != '0':  # Avoid adding '0' or repeating the same code
            result.append(code)
            prev_code = code

    return ''.join(result)

def generate_soundex(name):
    if not name:
        return ""
    soundex = process_name(name)
    return soundex[:4].ljust(4, '0')
