"""
#Lists

Brands=["Nike","Adidas", "Puma","Louis Vitton"]


# Add Item
Brands.append("Gucci")
# Remove Item
Brands.remove("Nike")
# Remove the Last Item
Brands.pop()
# Remove fastly
del Brands[2]

# Copy a list
Brands2=list(Brands)


# Join two or more lists
Brands2= ["Chanel", "Dior"]
Brands3= Brands+Brands2


HowMuch=len(Brands3)

Data="Amount: {}"


print(Data.format(HowMuch))
print(Brands3)


#INPUT AND LIST --------------------
# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)

"""
#Tupples and Unpacking

tup = (2,5,8)

#Convert array elements to simplify
a,b,c = tup

print(b)