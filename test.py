import itertools
import random

from tri import TriangleType

def test_permutations(a, b, c, typ):
    """Check all permutation on side length give the correct result"""
    perms = itertools.permutations([a,b,c])
    print("testing permutations of ", a, b, c)
    for t in perms:
        assert(typ == TriangleType.compute_type(*t))    # test call with several arguments
        assert(typ == TriangleType.compute_type(list(t)))  # test call with a list
        assert(typ == TriangleType.compute_type(t))     # test call with a tuple

def test_random_permutations():
    maxl = 100000.0
    for i in range(10000):
        a = random.uniform(0.0, maxl)
        b = random.uniform(0.0, maxl)
        c = random.uniform(0.0, maxl)
        typ = TriangleType.compute_type(a, b, c)
        test_permutations(a, b, c, typ)

def test():
    test_random_permutations()
    test_permutations(1, 1, 1, TriangleType.Equilateral)
    test_permutations(1, 1, 2, TriangleType.Isocele)
    test_permutations(1, 2, 3, TriangleType.Scalene)

if __name__ == '__main__':
    test()

