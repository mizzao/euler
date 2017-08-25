def sieve(limit):
    # Initialize list up to a limit
    a = [True] * limit
    a[0] = False
    a[1] = False

    for (i, prime) in enumerate(a):
        if prime:
            yield i
            # Iterate from square of number up to max
            for n in range(i*i, limit, i):
                a[n] = False
