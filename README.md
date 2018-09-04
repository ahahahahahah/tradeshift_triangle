# tradeshift_triangle
Triangle test in Tradeshift application procedure

Challenge:
  Write a program that will determine the type of a triangle. It should take the lengths of the triangle's three sides as input, and return whether the triangle is equilateral, isosceles or scalene.

Strategy:
    The function to decide the type of a triangle is a static method of a class (method 'compute_type' of class TriangleType). The class serves as a namespace to include parameters of the algorithm ('epsilon' to compare floating point lengths) and some named triangle types.
    A decorator around the method is added to provide syntactic sugar: the function can be called with a list/tuple of 3 numbers, or with 3 bare numbers.
    The function validates its input by checking that its arguments are numbers strictly higher than 0, throws an exception otherwise.

Tests:
    A small test suite is provided: the first test verifies one instance of each triangle type. A second test verifies that the function result does not depend on the argument order (used with randomly generated triangles).




