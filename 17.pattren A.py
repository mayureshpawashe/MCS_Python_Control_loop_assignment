#Write a Python program to print alphabet pattern 'A'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of A
    if i == 1:
        print(space + STAR * (width-2))
    # middle row of A
    elif i == int(height/2+1):
        print(STAR * width)
    # rest of A
    else:
        print(STAR + space * (width-2) + STAR)