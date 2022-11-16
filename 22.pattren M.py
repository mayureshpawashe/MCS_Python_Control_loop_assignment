#Write a Python program to print alphabet pattern 'M'.
width = 5 # must be an odd number for symmetry
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # middle of M
    if i == int(height/2+1):
        print(STAR + space * int((width-3)/2) + STAR + space * int((width-3)/2) + STAR)
    # row above middle of M
    elif i < int(height/2+1) and i > (int(height/4+1)):
        print(STAR + space * (i-3) + STAR + space * (width-4-2*(i-3)) + STAR + space * (i-3) + STAR)
    # rest of M
    else:
        print(STAR + space * (width-2) + STAR)