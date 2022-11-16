#Write a Python program to print alphabet pattern 'L'.
width = 5
height = width + 2
STAR = '*'
for i in range(1, height+1):
    # last row of G
    if i == height:
        print(STAR * width)
    # rest of G
    else:
        print(STAR)