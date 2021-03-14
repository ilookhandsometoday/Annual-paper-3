def encrypt(text, keygen):
    text_as_binary = "".join(_to_binary(text))
    hundred_bit_messages = []
    # message is split into chunks of 100 bits as per recommendations from Merkle and Hellman
    for hundred_bits in _chunk_text(text_as_binary):
        # a variable for the final sum
        encrypted_bits = 0
        for bit, open_key_element in zip(hundred_bits, keygen.open_key):
            encrypted_bits += int(bit) * open_key_element
        hundred_bit_messages.append(encrypted_bits)
    return hundred_bit_messages

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

def _chunk_text(text, length):
    """Separates text into chunks of given length"""
    return (text[0+i:length+i] for i in range(0, len(text), 100))

