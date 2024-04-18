from collections import Counter

mylist = [1,5,4,7,8,1,1,4]

print(Counter(mylist).keys())

while True:
    shoesN = int(input())
    sizesRaw = input()
    sizesLiq = sizesRaw.split()
    customers = int(input())
    n = 0
    while n < customers:

     shoeSize,price = input().split()
     priceInt = int(price)
     n+=1
    
