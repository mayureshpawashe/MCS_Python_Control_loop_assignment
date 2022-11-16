width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of T
    if i == 1:
        print(STAR * width)
    # rest of T
    else:
        print(space * int((width-1)/2) + STAR + space * int((width-1)/2))