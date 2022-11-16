#31. Write a Python program to calculate a dog's age in dog's years. Note: For the first two years
# , a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output: Input a dog's age in human years: 15 The dog's age in dog's years is 73
dog_age = float(input("Input a dog's age in human years: "))
dogs_years = float()
if dog_age <= 2:
    dogs_years = dog_age*10.5
else:
    dogs_years+=21+(dog_age-2)*4
print("The dog's age in dog's years is %.1f" % dogs_years)