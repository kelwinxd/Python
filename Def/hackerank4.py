def is_leap(year):
    leap = False
    
    if 1900<= year <= 10**5:
        if (year % 4 == 0) and (not (year % 100 ==0) or (year % 400 == 0)):
            leap = True
            print(leap)
        else:
            print(leap)
            
    
    else:
         print('insira um numero correto')

year = int(input())

is_leap(year)