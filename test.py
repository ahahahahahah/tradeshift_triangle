import itertools
import random

from tri import *

def test_permutations(a, b, c, typ):
    """Check all permutation on side length give the correct result"""
    perms = itertools.permutations([a,b,c])
    print("testing permutations of triangle (%s %s %s), type %s" % (a, b, c, typ))
    for t in perms:
        assert(typ == TriangleTyper.compute_type(*t))    # test call with several arguments
        assert(typ == TriangleTyper.compute_type(list(t)))  # test call with a list
        assert(typ == TriangleTyper.compute_type(t))     # test call with a tuple

def test_random_permutations_int():
    maxl = 100      # give a low range to raise the chances of getting isocele or equilateral picks
    for i in range(10000):
        a = random.randint(0, maxl)
        b = random.randint(0, maxl)
        c = random.randint(0, maxl)
        typ = TriangleTyper.compute_type(a, b, c)
        test_permutations(a, b, c, typ)

def test_random_permutations_float():
    maxl = 100000.0
    for i in range(10000):
        a = random.uniform(0.0, maxl)
        b = random.uniform(0.0, maxl)
        c = random.uniform(0.0, maxl)
        typ = TriangleTyper.compute_type(a, b, c)
        test_permutations(a, b, c, typ)

def test():
    test_random_permutations_int()

    test_random_permutations_float()

    test_permutations(1, 1, 1, TriangleType.Equilateral)
    test_permutations(1, 1, 2, TriangleType.Isocele)
    test_permutations(1, 2, 3, TriangleType.Scalene)

if __name__ == '__main__':
    test()

