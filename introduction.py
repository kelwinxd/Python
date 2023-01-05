
#commnets one line
""" multiple 
    lines
    comment
"""
print("Hello World")

name="John"
age=24

#cast operations
print(name + " has " + str(age) + " years old")

#Functions
#Scolp is identified by space
def licit():
 if age>18:
  print(name + " can Drive")
#execute the function
licit()  

#Types----------------------
x=8 #int
x="Hello" #string
x=True #Bool
x=3,14 #Float
x=['Shorts','Hat','Shoes'] #Array
x=('Shorts','Hat','Shoes') #Tuple (cant change)
x=range(0,100,2) #List counted 2 per 2, 0 until 100
x={
  "nome":"Kel",
  "height":1.85
}
x={8,6,8,5,7,8} #set

#Calling a array
#print("Value: " + x[0])

#Calling a object element
print("Value: " + x["nome"])

#identifing the type of date
print("Type: " + str(type(x)))

