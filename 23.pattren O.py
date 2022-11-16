#Write a Python program to print alphabet pattern 'O'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of O
    if i == 1 or i == height:
        print(space + STAR * (width-2))
    # rest of D
    else:
        print(STAR + space * (width-2) + STAR)