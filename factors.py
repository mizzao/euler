def divisors(num, proper=False):
    ds = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            ds.add(i)
            ds.add(num // i)
    
    if proper:
        ds.remove(num)
        
    return ds
