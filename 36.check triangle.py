#36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Note :
# An equilateral triangle is a triangle in which all three sides are equal. A scalene triangle is a
# triangle that has three unequal sides.An isosceles triangle is a triangle with (at least)
# two equal sides. Expected Output: Input lengths of the triangle sides: x: 6 y: 8 z: 12 Scalene triangle
x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

if x==y==z:
    print('Equilateral')
elif x!=y!=z:
    print('Scalene')
else:
    print('Isosceles')