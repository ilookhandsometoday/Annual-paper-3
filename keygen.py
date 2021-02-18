import random
import sys
import math

_RNG = random.SystemRandom()


class Keygen:

    def __init__(self):
        # seq is the sequence for the private key
        # I'm using 128 elements because that's gonna be the size of the chunks
        # that the original message is going to be split into for encryption
        self.seq = Keygen.generate_si_sequence(128)
        # modulus and multiplier are coprime numbers used for key generation
        self.modulus = Keygen._find_modulus(self.seq)
        self.multiplier = Keygen._find_multiplier(self.modulus)

        #self.open_key

    @staticmethod
    def generate_si_sequence(n):
        """Generates a superincreasing sequence of length n."""
        sequence = []
        s_sum = 0
        for i in range(n):
            sequence.append(_RNG.randint(1, sys.maxsize) + s_sum)
            s_sum = sum(sequence)
        return sequence

    @staticmethod
    def _find_multiplier(modulus):
        coprime = False
        multiplier = 0
        while not coprime:
            multiplier = _RNG.randint(2, modulus-1)
            if math.gcd(modulus, multiplier) == 1:
                coprime = True
        return multiplier

    @staticmethod
    def _find_modulus(seq):
        seq_sum = sum(seq)
        modulus = _RNG.randint(seq_sum + 1, seq_sum + sys.maxsize)
        return modulus
