phrase = 'Python is programation language \n created by Guido van rossum'

phrase_without_space = phrase.replace(' ', '')

most_appear = ''
how_many_counter = 0
i = 0 
most = []
while i < len(phrase_without_space):
    
    current_letter = phrase_without_space[i]
    how_many = phrase_without_space.count(current_letter)

    if how_many_counter < how_many:
        how_many_counter = how_many
        most_appear = current_letter

    
    i+=1
print(most_appear, how_many_counter)

    
   
