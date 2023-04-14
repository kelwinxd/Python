
#fazer ler a frase, contar o caracter que mais aparecem e mostrar



phrase = 'Kelwin Regis Esechiel'

i = 0
MostAppeared = ''
Times = 0

while i < len(phrase):
    Now_letter = phrase[i]

    if Now_letter == ' ':
        i += 1
        continue
    

    

    HowMuch_now = phrase.count(Now_letter)

    if Times < HowMuch_now:
        Times = HowMuch_now
        MostAppeared = Now_letter
    
    

    i += 1

print(f'{MostAppeared}, {Times}' )






    
    
 