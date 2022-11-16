#Write a Python program to print alphabet pattern 'G'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of G
    if i == 1 or i == height:
        print(space + STAR * (width-2))
    # row above middle of G except the second row
    elif i > 2 and i <= int(height/2):
        print(STAR)
    # middle of G
    elif i == int(height/2+1):
        print(STAR + space + STAR * (width-2))
    # rest of G
    else:
        print(STAR + space * (width-2) + STAR)