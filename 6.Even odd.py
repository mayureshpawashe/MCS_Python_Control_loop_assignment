#6. Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Output : Number of even numbers : 5
# Number of odd numbers : 4
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
odds_counter = 0
evens_counter = 0
for i in numbers:
    if i%2 == 0:
        evens_counter+=1
    else:
        odds_counter+=1

print('Number of even numbers: %d'% evens_counter)
print('Number of odd numbers: %d'% odds_counter)