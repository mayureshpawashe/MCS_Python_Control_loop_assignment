#Write a Python program to print alphabet pattern 'X'
width = 13  # must be an odd number for symmetry
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height + 1):
    # middle of X
    if i == int(height / 2 + 1):
        print(space * int((width - 1) / 2) + STAR + space * int((width - 1) / 2))

    # row above middle of X
    elif i < int(height / 2 + 1) and i > int(height / 4):
        print(space * (i - 2) + STAR + space * (width - 2 - 2 * (i - 2)) + STAR + space * (i - 2))

    # row below middle of X
    elif i > int(height / 2 + 1) and i <= int(height * 3 / 4 + 1):
        print(
            space * (width - i + 1) + STAR + space * (width - 2 - 2 * (width - i + 1)) + STAR + space * (width - i + 1))

    # rest of M (first rows and last rows)
    else:
        print(STAR + space * (width - 2) + STAR)