#Make a runnerup finder

a = True
n = int(input())
arr = []
while a:
    for n in range(n):
        scores = int(input())
        arr.append(scores)
    a = False
arr.sort(reverse=True)
set_list = list(set(arr)) #set drops the duplicate numbers
set_list.sort(reverse=True)
print(f'the second item is {set_list[1]} of {arr}')
