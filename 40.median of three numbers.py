#Write a Python program to find the median of three values. Expected Output: Input first number: 15 Input
# second number: 26 Input third number: 29 The median is 26.0
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

if (x>=y and x<=z) or (x>=z and x<=y):
    median=x
elif (y>=x and y<=z) or (y>=z and y<=x):
    median=y
else:
    median=z
print('The median is', median)