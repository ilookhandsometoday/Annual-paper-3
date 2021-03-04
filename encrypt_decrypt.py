def encrypt(text, keygen):
    text_as_binary = _to_binary(text)
    for char_as_bits in text_as_binary:
        pass
    pass

def decrypt(text, keygen):
    pass

def _to_binary(text):
    """Returns a list of characters of the original text in binary form using UTF-8 encoding"""
    as_bytes = bytearray(text, "utf-8")
    binary_values = list(map(lambda byte: bin(byte)[2:], as_bytes))
    return binary_values