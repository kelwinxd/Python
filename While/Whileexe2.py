index = 0
name = 'kelwin regis'
new_name = ''
while index < len(name):
    
    letter = name[index]
    new_name += '*' + letter
    index +=1

print(new_name)