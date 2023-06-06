
#Args allow input ilimited argments
def sumAll(*args):
    total = 0
    args = list(args)
    for n in args:
        total += int(n)
    return total

numbers = 1,5,4,6
print(sumAll(2,5,2,10,4))


#when u use * before a tuple or list, it will unpack the numbers, letting them 
# spread
print(sumAll(*numbers))





print(sum(numbers))