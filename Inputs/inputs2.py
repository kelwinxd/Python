
#Current Conversor

Value = int(input("Real: $ "))
Current = input("(D) Dolar \n(E) Euro \n")

if Current.upper() =='D':
    print(f'Your value in Dolar is: {round(Value/5.17, 2)} U$')
elif Current.upper() =='E':
    print(f'Your value in Euro is: {round(Value/5.54, 2)} U$')
else:
    print("Unknow Character")



