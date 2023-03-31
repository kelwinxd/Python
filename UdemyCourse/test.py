nome = input("Whats your name?")




if nome.isdigit():
 print('Error, return a valid name')
else:
 if len(nome) >= 0 and len(nome) <= 4:
  print("Short Name")
 elif len(nome) >= 5 and len(nome) <= 6:
  print("Normal Name")
 elif len(nome) > 6:
  print("Huge Name")
 else:
  print('Unknown format')

 
 
 

   

