import math
from decorators import *
import numbers

from enum import Enum     # for enum34, or the stdlib version
TriangleType = Enum('TriangleType', 'Scalene Isocele Equilateral')


class TriangleTyper:
    """Helper class to decide a triangle type: Equilateral, Isocele or Scalene"""
    epsilon = 1e-6      # tolerance for equality of lengths

    @staticmethod
    @list_unfolder
    def compute_type(a, b, c):
        assert(isinstance(a, numbers.Real))
        assert(isinstance(b, numbers.Real))
        assert(isinstance(c, numbers.Real))
        assert(a >= 0)
        assert(b >= 0)
        assert(c >= 0)

        # side length differences
        Dab = math.fabs(a-b)
        Dac = math.fabs(a-c)
        Dbc = math.fabs(b-c)

        # shorter synonym for readability
        e = TriangleTyper.epsilon

        # Default to scalene
        typ = TriangleType.Scalene

        # Check how many side are equal (length difference is 0 or very small)
        if Dab < e and Dac < e:
            # 2 length equalities means all three sides are equal
            assert(Dbc < e)
            typ = TriangleType.Equilateral
        elif Dab < e or Dac < e or Dbc < e:
            # one length equality
            typ = TriangleType.Isocele

        return typ
        

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: python %s <a> <b> <c>\n  where a, b, c are the triangle side lengths." % sys.argv[0])
        sys.exit(-1)

    # extract parameters and convert from string to float 
    side_lengths = [float(sys.argv[i]) for i in range(1,4)]

    # decide triangle type
    typ = TriangleTyper.compute_type(side_lengths)
    print(typ)

