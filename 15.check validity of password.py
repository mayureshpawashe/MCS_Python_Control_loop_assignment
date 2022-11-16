#15. Write a Python program to check the validity of password input by users. Validation: • At least 1
# letter between [a-z] and 1 letter between [A-Z]. • At least 1 number between [0-9]. •
# At least 1 character from [$#@]. • Minimum length 6 characters. • Maximum length 16 characters.
password = input('please enter a valid password: ')
while True:
    length, digits, lowers, uppers, characters = 0, 0, 0, 0, 0
    if len(password) > 6 and len(password) < 16:
        length = 1
    for i in password:
        if i.isdigit():
            digits = 1
            continue
        if i.islower():
            lowers = 1
            continue
        if i.isupper():
            uppers = 1
            continue
        if i in '$#@':
            characters = 1
            continue
    rules = [length, digits, lowers, uppers, characters]
    if all(rules): #all function return boolean value return true(1) and False(0)
        print('your password is good')
        break
    else:
        print('your password is not good, try again')
        password = input('please enter a valid pasword: ')