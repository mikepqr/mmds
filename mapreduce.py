def prime_factors(n):
    # pinched from
    # http://stackoverflow.com/questions/15347174/python-finding-prime-factors
    # set() function added to ensure uniqueness in return
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)


def reducer(k, v):
    return (k, sum(v))


def grouper(l):
    d = {}
    for i, j in l:
        if i in d:
            d[i].append(j)
        else:
            d[i] = [j]
    return d


def homework4():
    xx = [15, 21, 24, 30, 49]
    out = []
    for x in xx:
        pf = prime_factors(x)
        out += zip(pf, [x]*len(pf))
    for k, v in grouper(out).items():
        print reducer(k, v)
