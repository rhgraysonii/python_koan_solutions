#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    equilateral, scalene, isosceles = check_triangles(a, b, c)
    check_neg_and_zero([a, b, c])
    if equilateral:
        return 'equilateral' 
    elif isosceles:
        return 'isosceles' 
    elif scalene:
        return 'scalene'
    else:
        pass

def check_neg_and_zero(side_list):
    for side in side_list:
        if side <= 0:
            raise TriangleError

def check_triangles(a, b, c):
    x = check_equilateral(a, b, c)
    y = check_scalene(a, b, c)
    z = check_isosceles(a, b, c)
    return x, y, z
    
def check_equilateral(a, b, c):
    if a == b and a == c:
        return True
    else:
        return False

def check_scalene(a, b, c):
    if a != b and a != c and b != c:
        return True
    else:
        return False

def check_isosceles(a, b, c):
    if a == b or b == c or a == c and check_scalene(a,b,c) == False:
        return True
    else:
        return False
        
# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
