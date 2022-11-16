#Write a Python program to print alphabet pattern 'P'.
width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and middle row of P
    if i == 1 or i == int(height/2+1):
        print(STAR * (width-1))
    # rows between first and middle row of P
    elif i > 1 and i < int(height/2+1):
        print(STAR + space * (width-2) + STAR)
    # lower part of P
    else:
        print(STAR)