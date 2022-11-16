#16. Write a Python program to find numbers between 100 and 400 (both included) where each
# digit of a number is an even number. The numbers obtained should be printed in a comma-separated
# sequence.
evens_list = []
for i in range(100,401):
    number=i
    while number>0:
        digit=number%10
        if digit%2==0:
            number=number//10
            even=True
        else:
            even=False
            break
    if even:
        evens_list.append(i)
print(', '.join(map(str, evens_list)))