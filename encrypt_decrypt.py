def encrypt(text, keygen):
    text_as_binary = _to_binary(text)
    for char_as_bits in text_as_binary:
        pass

def decrypt(text, keygen):
    pass

def _to_binary(text):
    """Returns a list of characters of the original text in binary form using UTF-8 encoding"""
    as_bytes = bytearray(text, "utf-8")
    binary_values = list(map(lambda byte: bin(byte)[2:], as_bytes))
    #This is done to make it easier to separate the decrypted message into 8 bit chunks, since bin()
    #removes leading zeros from a binary representation of a byte
    binary_values_uniform = []
    for char_as_bits in binary_values:
        missing_zeroes = 8 - len(char_as_bits)
        new_char_as_bits = missing_zeroes*"0" + char_as_bits
        binary_values_uniform.append(new_char_as_bits)
    return binary_values_uniform