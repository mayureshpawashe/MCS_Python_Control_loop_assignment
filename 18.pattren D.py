#Write a Python program to print alphabet pattern 'D'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of D
    if i == 1 or i == height:
        print(STAR * (width-1))
    # rest of D
    else:
        print(STAR + space * (width-2) + STAR)