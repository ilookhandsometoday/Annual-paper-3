import keygen

def encrypt(text, keygen):
    text_as_binary = _to_binary(text)
    pass

def decrypt(text, keygen):
    pass

def _to_binary(text):
    as_bytes = bytearray(text, "utf-8")
    binary_values = []
    for byte in as_bytes:
        binary_values.append(bin(byte)[2:])

    return binary_values