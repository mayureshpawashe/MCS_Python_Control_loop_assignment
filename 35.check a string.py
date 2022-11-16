#35. Write a Python program to check a string represent an integer or not. Expected Output:
# Input a string: Python The string is not an integer.
str=input("Enter String::")
f=False
for i in str:
    if i.isdigit():
        f=True

    else:
        f=False
if f==True:
    print("String Contain Integer value")
else:
    print("the string is not an integer")