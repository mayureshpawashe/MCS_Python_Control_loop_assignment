#Write a Python program to print alphabet pattern 'U'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # last row of U
    if i == height:
        print(space + STAR * (width-2) + space)
    else:
        print(STAR + space * (width-2) + STAR)