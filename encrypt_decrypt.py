#TODO change methods to accomodate for keys that are not provided by keygen
def encrypt(text, keygen, open_key=[]):
    """Ecnrypts text by using the given Merkle-Hellman key generator
    or a given open key.
    Returns a list of encrypted 100-bit(or less) chunks of the original message"""
    if open_key:
        _open_key = open_key
    else:
        _open_key = keygen.open_key

    text_as_binary = "".join(_to_binary(text))
    encrypted_chunks = []
    # message is split into chunks of 100 bits as per recommendations from Merkle and Hellman
    for chunk in _chunk_text(text_as_binary, 100):
        # a variable for the final sum
        encrypted_chunk = 0
        for bit, open_key_element in zip(chunk, _open_key):
            encrypted_chunk += int(bit) * open_key_element
        encrypted_chunks.append(encrypted_chunk)
    return encrypted_chunks


def decrypt(encrypted_chunks, keygen, sequence=[], multiplier=None, modulus=None):
    """Decrypts the encrypted 100-bit(or less) chunks that are output by encrypt()
    using the given key generator or a given private key.
    Returns the original text"""
    if sequence and multiplier is not None and modulus is not None:
        _seq = sequence
        _multiplier = multiplier
        _modulus = modulus
        _multiplier_mod_inverse = pow(multiplier, -1, modulus)
    else:
        _seq = keygen.seq
        _multiplier = keygen.multiplier
        _modulus = keygen.modulus
        _multiplier_mod_inverse = keygen.multiplier_mod_inverse

    decrypted_chunks = []
    for e_chunk in encrypted_chunks:
        target_sum = e_chunk * _multiplier_mod_inverse % _modulus
        indices_of_ones = []
        for element in reversed(_seq):
            if element <= target_sum:
                target_sum = target_sum - element
                indices_of_ones.append(_seq.index(element))
        decrypted_chunks.append(_restore_chunk(indices_of_ones))
    decrypted_message = "".join(decrypted_chunks)
    decrypted_message_bytes = _chunk_text(decrypted_message, 8)
    source_text = _to_text(decrypted_message_bytes).rstrip("\x00")
    return source_text


def _to_binary(text):
    """Returns a list of characters of the original text in binary form using UTF-8 encoding"""
    as_bytes = bytearray(text, "utf-8")
    binary_values = list(map(lambda byte: bin(byte)[2:], as_bytes))
    # This is done to make it easier to separate the decrypted message into 8 bit chunks, since bin()
    # removes leading zeros from a binary representation of a byte
    binary_values_uniform = [(8 - len(char_as_bits))*"0" + char_as_bits for char_as_bits in binary_values]
    return binary_values_uniform


def _to_text(text_as_bytes):
    """Transforms an iterable of bytes in binary form into a text using UTF-8 encoding"""
    # turn a binary representation of a byte into an integer to later turn it into a byte array
    bytes_as_integers = (int(byte, 2) for byte in text_as_bytes)
    byte_array = bytearray(bytes_as_integers)
    text = byte_array.decode("utf-8")
    return text


def _chunk_text(text, length):
    """Separates text into chunks of given length and returns a generator"""
    return (text[0+i:length+i] for i in range(0, len(text), length))


def _restore_chunk(indices_of_ones):
    """Restores a 100 bit chunk from a list of indices of 1 in a chunk"""
    restored_chunk = ""
    for i in range(100):
        if i in indices_of_ones:
            restored_chunk = restored_chunk + "1"
        else:
            restored_chunk = restored_chunk + "0"
    return restored_chunk


