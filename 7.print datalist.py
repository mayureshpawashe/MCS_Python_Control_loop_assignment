#Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, "Moderncollege", (0, -1), [5, 12],{"class":'V', "section":'A'}]
for i in datalist:
    print(i, type(i))