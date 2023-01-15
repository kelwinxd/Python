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

