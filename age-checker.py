print('hello humans!')
age = int(input('how old are you?'))
if age < 12:
    print('you are too young')
elif age >= 12 and age <= 20:
    print('Teen access granted!')
elif age > 20:
    print('welcome adult user!')