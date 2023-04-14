

Products=["Hat","Pants","Shirt"]


"""
for x in Products:
    print(x)
    if(x=="Shirt"):
        Products.append("Shoes")
           
        

#With Numbers

for number in range(1,10,2):
    print("Test", number,number * ".")

    
#Child For Looping
for x in range(1,6):
   for y in range(1,4):
    print(f"({x}, {y})")

        """

#Summing
"""
Values=[20,40,60,80]
total=0

for Value in Values:
    total+=Value

print(f"Total: {total}")

#repiting char

numbers=[5,2,3]

for num in numbers:
    print(num * "x")


n = [8,3,6]

#Ascending Order
n.sort()

#Descending Order
n.reverse()

#Insert(Position, Value)
n.insert(1,7)

print(n)
"""

#Program to remove numbers duplicated
array = [10,2,2,3,6]
array2 =[]

for x in array:
    if x not in array2:
        array.append(array)
print(array2)



