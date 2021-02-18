import random
import sys


def generate_si_sequence():
    """generates a superincreasing sequence of length 128.
    Number 128 is chosen to ensure security by virtue of making it harder to guess the key and also by making a birthday attack practically impossible"""
    sysrand = random.SystemRandom()
    sequence = []
    s_sum = 0
    for i in range(128):
        sequence.add(sysrand.randint(1, sys.maxsize) + s_sum)
        s_sum = sum(sequence)
    return sequence

