#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue'
# statement. Expected Output : 0 1 2 4 5
for i in range(7):
    if i == 3 or i == 6:
        continue  #continue skip that iteration and move to next iteration
    print(i,end='')