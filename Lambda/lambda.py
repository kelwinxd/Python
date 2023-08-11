list = [{"first_name":"Raymund","Age":22},
{"first_name":"Dreddy","Age":21},
{"first_name":"Trefor","Age":35},
{"first_name":"Mikey","Age":42},
{"first_name":"Almire","Age":58}]
#Lambda is one line anonymous code

#you can write a function name or use a lambda
list.sort(key=lambda item:item['first_name'])

for  name in list:
    print(f'Name: {name.get("first_name")}, Age: {name.get("Age")}')