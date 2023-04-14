#Enter the multiple number



end = int(input('which number do you want to see the multiple? '))
multiple = int(input('Enter the Multiple: '))

number = range(0, end, multiple)

for n in number:
    print(n)

print(f'Theres {len(number) - 1} multiples of {multiple} until {end}')
    

