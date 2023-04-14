



while True:
    n1 = input('Number 1: ')
    n2 = input('Number 2: ')
    op = input('Operator: ')
    valid_number = None
    nFloat = 0
    n2Float = 0

    try:
        nFloat = float(n1)
        n2Float = float(n2)
        valid_number = True
    
    except:
        valid_number = None

    if valid_number is None:
        print('Some of these number are invalid')
        continue

    alowed_op = '+-/*'

    if op not in alowed_op:
        print('Invalid operator, please try +-/*')
        continue
    if len(op) > 1:
        print('Type just one operator')
        continue


    if op == '+':
        print(nFloat + n2Float)
    elif op == '-':
        pass
    elif op == '*':
        pass
    elif op == '/':
        pass

    quit = input('If you want to Quit type [x]: ').lower()
    if quit == 'x':
        break
    else:
        print('please type x to quit')
    

