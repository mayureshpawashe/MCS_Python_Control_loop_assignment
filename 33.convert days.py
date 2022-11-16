#33. Write a Python program to convert month name to a number of days. Expected Output:
# List of months: January, February, March, April, May, June, July, August , September, October, November
# , December Input the name of Month: February No. of days: 28/29 days
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
month = input('Enter Month  ').title() #title return first char of string is upper case
if month in months:
    if month == 'February':
        print('No. of days: 28/29 days')
    elif month in ('April', 'June', 'September', 'November'):
        print('No. of days: 30 days')
    else:
        print('No. of days: 31 days')
else:
    print('you enter a wrong month name')