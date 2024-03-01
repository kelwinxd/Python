import os

market_list = []
while True:
    initial = input("[i]nsert [l]ist [d]elete: \n")
    if initial.lower() == "i":
        os.system('cls')
        insertion = input("Insert a item:")
        market_list.append(insertion)
        print("added succesfully!")
        
    elif initial.lower() == "l":
        os.system('cls')
        if len(market_list) > 0:
         for index, i in enumerate(market_list):
            print(index, i)
        else:
           print("Any item")
    elif initial.lower() == "d":
       os.system('cls')
       index_string = input("index for delete?: ")
       try:
         index_delete = int(index_string)
         del market_list[index_delete]
       except ValueError:
          print("Please enter a valid value")
       except IndexError:
          print("this index doenst exist")
       os.system('cls')
       print("deleted!")
       
             
          
       



