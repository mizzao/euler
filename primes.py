import numpy as np
from math import ceil

def sieve(limit):
    numbers = np.arange(limit)
    sieve = np.ones(limit, dtype=bool)

    sieve[0] = False
    sieve[1] = False

    for n in range(ceil(np.sqrt(limit))):
        if sieve[n]:
            sieve[n*n::n] = False

    return numbers[sieve]
