#Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# [Formula: c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ] Expected
# Output : 60°C is 140 in Fahrenheit 45°F is 7 in Celsius
t=int(input("Enter Tempreture::"))
u=input("Enter C for celsis and F for Fahrenheit you want to convert::").upper()
if u=='C':
    c=float((t*1.8)+32)
    print("Tempreture in celcius :: %f"%c)
elif u=='F':
    f=float((t-32)*5/9)
    print("Tempreture in Fahrenheit is ::%f"%f)