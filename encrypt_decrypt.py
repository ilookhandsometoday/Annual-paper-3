def encrypt(text, keygen):
    """Ecnrypts text by using the given Merkle-Hellman key generator.
    Returns a list of encrypted 100-bit(or less) chunks of the original message"""
    text_as_binary = "".join(_to_binary(text))
    encrypted_chunks = []
    # message is split into chunks of 100 bits as per recommendations from Merkle and Hellman
    for chunk in _chunk_text(text_as_binary, 100):
        # a variable for the final sum
        encrypted_chunk = 0
        for bit, open_key_element in zip(chunk, keygen.open_key):
            encrypted_chunk += int(bit) * open_key_element
        encrypted_chunks.append(encrypted_chunk)
    return encrypted_chunks


def decrypt(encrypted_chunks, keygen):
    for e_chunk in encrypted_chunks:
        pass


def _to_binary(text):
    """Returns a list of characters of the original text in binary form using UTF-8 encoding"""
    as_bytes = bytearray(text, "utf-8")
    binary_values = list(map(lambda byte: bin(byte)[2:], as_bytes))
    #This is done to make it easier to separate the decrypted message into 8 bit chunks, since bin()
    #removes leading zeros from a binary representation of a byte
    binary_values_uniform = [(8 - len(char_as_bits))*"0" + char_as_bits for char_as_bits in binary_values]
    return binary_values_uniform


def _chunk_text(text, length):
    """Separates text into chunks of given length"""
    return (text[0+i:length+i] for i in range(0, len(text), length))

