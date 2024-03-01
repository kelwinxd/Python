n = int(input('digite:'))
entry = input()

values = entry.split()
sheet = []

if len(values) == n:
    print('you right')
    for i in values:
        num = int(i)
        if num > num:
            print(num)

else:
    print('wrong')