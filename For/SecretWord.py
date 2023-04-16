


import os






secret= 'monkey'
earned_words = ''
repetition = 0
limit = 6

while True:
    type_word = input('Type up: ')

    if len(type_word) > 1:
        print('Type just one Letter')
        continue

    

    if repetition > limit:
        print('You failed, 3 attempts')
        break

    if type_word in secret:
        earned_words += type_word
    
    full_word = ''
    
    
    
    for letter in secret:
        if letter in earned_words:
            full_word += letter
        else:
            
            full_word += '*'
    
    print(f'Full word for now is: {full_word}')

    if full_word == secret:
        os.system('clear')
        print('You Won!!! Congrats')
        print(full_word)
        earned_words = ''

   