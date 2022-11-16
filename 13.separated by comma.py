#13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data: 0100,0011,1010,1001,1100,1001 Expected Output : 1010
my_bins=input("Enter Binary Number:: ")
input_bins=my_bins.split(',')
output_bins=[]

for i in input_bins:
    if int(i,base=2)%5==0:
        output_bins.append(i)

print(','.join(output_bins))