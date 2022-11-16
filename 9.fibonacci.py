#Write a Python program to get the Fibonacci series between 0 to 50. Note : The Fibonacci Sequence
# is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... Every next number is found by adding up
# the two numbers before it. Expected Output : 1 1 2 3 5 8 13 21 34
fib_list=[1,1]
while fib_list[-1]<=50:
    fib_list.append(fib_list[-1]+fib_list[-2])
print(fib_list[:-1])