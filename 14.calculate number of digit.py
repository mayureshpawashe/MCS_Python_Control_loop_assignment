#14. Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2 Expected Output : Letters 6 Digits 2
str=input("Enter String with Digit::")
cnt_digit=0
cnt_char=0
for i in str:
    if i.isalpha():
        cnt_char=cnt_char+1

    if i.isdigit():
        cnt_digit=cnt_digit+1

print("Number Of Digit:: %d"%cnt_digit)
print("Number Of Characters:: %d"%cnt_char)
