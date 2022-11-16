#Write a Python program to print alphabet pattern 'Z'.
width = 7
height = width
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of Z
    if i == 1 or i == height:
        print(STAR * width)
    # rest of Z
    else:
        print(space * (width-i) + STAR + space * (i-1))