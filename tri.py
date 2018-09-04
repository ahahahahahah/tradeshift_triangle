import math
from decorators import *

class TriangleType:
    """Helper class to decide a triangle type: Equilateral, Isocele or Scalene"""
    epsilon = 1e-6      # tolerance for equality of lengths

    Scalene     = 0     # There might be an enum type in newer python versions, must check
    Isocele     = 1
    Equilateral = 2

    @staticmethod
    @list_unfolder
    def compute_type(a, b, c):
        assert(a >= 0)
        assert(b >= 0)
        assert(c >= 0)

        # side length differences
        Dab = math.fabs(a-b)
        Dac = math.fabs(a-c)
        Dbc = math.fabs(b-c)

        # shorter synonym for readability
        e = TriangleType.epsilon

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
        

