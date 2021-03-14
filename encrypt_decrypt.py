def encrypt(text, keygen):
    pass

def decrypt(text, keygen):
    pass

def _to_binary(text):
    """Returns a list of characters of the original text in binary form using UTF-8 encoding"""
    as_bytes = bytearray(text, "utf-8")
    binary_values = list(map(lambda byte: bin(byte)[2:], as_bytes))
    #This is done to make it easier to separate the decrypted message into 8 bit chunks, since bin()
    #removes leading zeros from a binary representation of a byte
    binary_values_uniform = [(8 - len(char_as_bits))*"0" + char_as_bits for char_as_bits in binary_values]
    return binary_values_uniform

