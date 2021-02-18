import random
import math

_RNG = random.SystemRandom()


class Keygen:

    def __init__(self):
        # seq is the sequence for the private key
        self.seq = Keygen.generate_si_sequence()
        # modulus and multiplier are coprime numbers used for key generation
        self.modulus = Keygen._find_modulus()
        self.multiplier = Keygen._find_multiplier(self.modulus)

        #self.open_key

    @staticmethod
    def generate_si_sequence():
        """Generates a superincreasing sequence according to recommendations from
        \"Hiding information and signatures in trapdoor knapsacks\""""
        sequence = []
        for index in range(1, 100, 1):
            lower_bound = (2 ** (index - 1) - 1) * (2 ** 100) + 1
            upper_bound = (2 ** (index - 1))*(2**100)
            sequence.append(_RNG.randint(lower_bound, upper_bound))
        return sequence

    @staticmethod
    def _find_multiplier(modulus):
        """Finds a multiplier almost according to recommendations from
        \"Hiding information and signatures in trapdoor knapsacks.\"
        Almost, because the method for making sure that multiplier is
        coprime with the modulus proposed in the paper does not work"""
        coprime = False
        multiplier = 0
        while not coprime:
            multiplier = _RNG.randint(2, modulus - 2)
            if math.gcd(modulus, multiplier) == 1:
                coprime = True
        return multiplier

    @staticmethod
    def _find_modulus():
        """Finds a modulus according to recommendations from
               \"Hiding information and signatures in trapdoor knapsacks\""""
        modulus = _RNG.randint((2**201) + 1, (2**202) - 1)
        return modulus
