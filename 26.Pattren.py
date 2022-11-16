#Write a Python program to print the following patterns.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of S
    if i == 1:
        print(space + STAR * (width-1))
    # middle row of S
    elif i == int(height/2+1):
        print(space + STAR * (width-2) + space)
    # last row of S
    elif i == height:
        print(STAR * (width-1) + space)
    # rows above middle row of S (exept first row)
    elif i > 1 and i < int(height/2+1):
        print(STAR)
    else:
        print(space * (width-1) + STAR)

width = 4
height = width + 1
STAR = 'ooo'
space = ' '
for i in range(1, height+1):
    # first, last and middle row of S
    if i == 1 or i == height or i == int(height/2+1):
        for j in range(3):
            print(STAR * width)
    # rows between first and middle row of S
    elif i > 1 and i < int(height/2+1):
        for j in range(3):
            print(STAR)
    # rows below middle of S
    else:
        for j in range(3):
            print(space * (width-1)*3 + STAR)