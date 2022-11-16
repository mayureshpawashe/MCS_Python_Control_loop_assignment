#34. Write a
# Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
int1 = int(input('integer 1: '))
int2 = int(input('integer 2: '))
def sum_of_integers(i,j):
    sum_of_int = i+j
    if sum_of_int in range(15, 21):
        return 20
    else:
        return sum_of_int
print(sum_of_integers(int1, int2))