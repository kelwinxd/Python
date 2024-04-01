try:
    file = open("data.txt", "a")
    content = file.write('\nHello world 3')
    print(content)
    value = True
    
except Exception as err:
    print(f'Error ocurred {err}')
    value = False


finally:
    
    test = 'successfully' if value else 'Fix the error'
    print(f'{test}, thanks')
    