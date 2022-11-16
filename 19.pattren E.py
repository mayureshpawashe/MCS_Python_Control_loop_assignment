#Write a Python program to print alphabet pattern 'E'.
width = 5
height = width + 2
STAR = '*'
for i in range(1, height+1):
    # first and last row of E
    if i == 1 or i == height:
        print(STAR * width)
    # middle of E
    elif i == int(height/2+1):
        print(STAR * (width-1))
    # rest of E
    else:
        print(STAR)