#Create a list which you can append, remove and list
import os

List = ['Item1']

"""
try:
    while True:
        entry = input('Press [a]dd [r]emove [l]ist: ')
        if entry.lower() == 'a':
            add = input('Type what you wanna add: ')
            List.append(add)
        elif entry.lower() == 'r':
                
            
            rem = int(input('Type what index you want to remove: '))
            
                
                
            List.remove(List[rem])
        elif entry.lower() == 'l':
            for i in enumerate(List):
                index, value = i
                print(index, value)
        elif entry.isdigit:
            print('Please type a character')
            continue


        if List == []:
            print('Empty List')
            continue
except ValueError:
    print('please type correct value')
    while True:
        entry = input('Press [a]dd [r]emove [l]ist: ')
        if entry.lower() == 'a':
            add = input('Type what you wanna add: ')
            List.append(add)
        elif entry.lower() == 'r':
                
            
            rem = int(input('Type what index you want to remove: '))
            
                
                
            List.remove(List[rem])
        elif entry.lower() == 'l':
            for i in enumerate(List):
                index, value = i
                print(index, value)
        elif entry.isdigit:
            print('Please type a character')
            continue


        if List == []:
            print('Empty List')
            continue
     """


while True:
        entry = input('Press [a]dd [r]emove [l]ist: ')
        if entry.lower() == 'a':
            os.system('cls')
            add = input('Type what you wanna add: ')
            if add in List:
                print('This already exists')
                continue
            List.append(add)
        elif entry.lower() == 'r':
         try:        
            
            rem = int(input('Type what index you want to remove: '))
            List.remove(List[rem])
         except ValueError:
             print('Please try a number')
         except IndexError:
             print('Index doesnt exist')
        elif entry.lower() == 'l':
            for i in enumerate(List):
                index, value = i
                print(index, value)
        elif entry.isdigit:
            print('Please type a character')
            continue
        else:
             print('Please try [a], [r] or [l]')
             continue


        if List == []:
            print('Empty List')
            continue

