name = 'Kelwin Regis'
counter = 0
new_string = ''

while counter < len(name):
    new_string += f'*{name[counter]}'
    
    counter+=1
print(new_string+"*")