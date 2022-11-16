#Write a Python program to
# construct the following pattern, using a nested for loop.
n = int(input('Enter Width:: '))
for i in range(1,n):
    print('*'*i)
for i in range(n,0,-1):
    print('*'*i)