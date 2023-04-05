x = 1
"""
while x <=10:
    print(x * "k")
    x+=1

print("Done Math")

# Password Little System 
"""

right=9
repetion=0
limit=3

while repetion < limit:
    password=int(input("Enter your password: "))
    repetion+=1
    if password==right:
        print("Correct Password!")
        break
    else:
        print("Incorrect Password")
else:
    print("3 Attempts limit, You Failed")

