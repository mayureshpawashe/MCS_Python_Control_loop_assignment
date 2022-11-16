#42. Write a Python program to calculate the sum and average of n integer numbers (input from the user).
# Input 0 to finish.
n=int(input("Enter how many numbers(Limit)::"))
tot=0
for i in range(0,n):
    num=int(input("Enter Number::"))
    tot=tot+num
avg=float(tot/n)
print("Total :: %d"%tot)
print("Average :: %f"%avg)