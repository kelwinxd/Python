
try:
    age = int(input('Your age: '))
    Division = 245 / age


except ZeroDivisionError:
    print('Division per Zero is forbidden')

except ValueError:
    print('Invalid Type of date')


