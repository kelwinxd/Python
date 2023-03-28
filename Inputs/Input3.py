Nome = input("Type your Full name: ")
Age = int(input("Type your age: "))

if Nome and Age:
    print(f"Your inverted name is: {Nome[::-1]}")
    print(f"Your name has {len(Nome)} characters")
    
    print(f"The last letter of your name is {Nome[-1]}")
    if " " in Nome:
        print("Your name has spaces")
    else: 
        print("Your name doesnt have spaces")
else:
    print("Sorry, you didnt typed")