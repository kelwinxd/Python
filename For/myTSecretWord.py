#Secret Word Exercise


secret = "monkey"



result = ''
repetition = 0
game = True
limit = 10


while repetition < limit:
 answer = input('Type up a word: ')
 repetition += 1
 for i in answer:
    if i in secret:
        
        result += i
        print(f'{i}, the word for now is {result}')

    elif i not in secret:
        
        
        print('Try again')
        continue
    
    if result == secret:
        print('You guessed! The word is ' + secret)
        game = False
        
    
else:
   print('3 attempts, you failed')
        



