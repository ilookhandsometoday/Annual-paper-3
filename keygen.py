import random
import math

_RNG = random.SystemRandom()


class Keygen:

    def __init__(self):
        # seq is the sequence for the private key
        self._seq = []
        # modulus and multiplier are coprime numbers used for key generation
        self._modulus = 0
        self._multiplier = 0
        self._open_key = 0

        self._generate_si_sequence()
        self._find_modulus()
        self._find_multiplier()
        self._find_open_key()
        self._find_multiplier_mod_inverse()

    @property
    def seq(self):
        return self._seq.copy()

    @property
    def modulus(self):
        return self._modulus

    @property
    def multiplier(self):
        return self._multiplier

    @property
    def open_key(self):
        return self._open_key

    @property
    def multiplier_mod_inverse(self):
        return self._multiplier_mod_inverse

    def _generate_si_sequence(self):
        """Generates a superincreasing sequence according to recommendations from
        \"Hiding information and signatures in trapdoor knapsacks\""""
        sequence = []
        for index in range(1, 100, 1):
            lower_bound = (2 ** (index - 1) - 1) * (2 ** 100) + 1
            upper_bound = (2 ** (index - 1))*(2**100)
            sequence.append(_RNG.randint(lower_bound, upper_bound))
        self._seq = sequence

    def _find_multiplier(self):
        """Finds a multiplier almost according to recommendations from
        \"Hiding information and signatures in trapdoor knapsacks.\"
        Almost, because the method for making sure that multiplier is
        coprime with the modulus proposed in the paper does not work"""
        coprime = False
        multiplier = 0
        while not coprime:
            multiplier = _RNG.randint(2, self._modulus - 2)
            if math.gcd(self._modulus, multiplier) == 1:
                coprime = True
        self._multiplier = multiplier

    def _find_modulus(self):
        """Finds a modulus according to recommendations from
               \"Hiding information and signatures in trapdoor knapsacks\""""
        modulus = _RNG.randint((2**201) + 1, (2**202) - 1)
        self._modulus = modulus

    def _find_open_key(self):
        self._open_key = [self._multiplier * number % self._modulus for number in self._seq]

    def _find_multiplier_modular_inverse(self):
        self._multiplier_modular_inverse = pow(self._multiplier, -1, self._modulus)


