import random
import sys
import math

_RNG = random.SystemRandom()


class Keygen:

    def __init__(self):
        # w is the sequence for the private key
        # I'm using 128 elements because that's gonna be the size of the chunks
        # that the original message is going to be split into for encryption
        self.w = Keygen.generate_si_sequence(128)
        self.q = Keygen._find_q(self.w)
        self.r = Keygen._find_r(self.q)

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
    def _find_r(q):
        coprime = False
        r = 0
        while not coprime:
            r = _RNG.randint(2, q-1)
            if math.gcd(q, r) == 1:
                coprime = True
        return r

    @staticmethod
    def _find_q(w):
        w_sum = sum(w)
        q = _RNG.randint(w_sum + 1, w_sum + sys.maxsize)
        return q
