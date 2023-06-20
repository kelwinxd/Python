quetions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#for index,value in quetions[0].items():
 #   print(index,value)


rights = 0
wrongs = 0
for q in quetions:

    
    print('Quetions: ', q['Pergunta'])
    for i, option in enumerate(q['Opções']):
        def var(index):
            if index == 0:
                return 'a)'
            elif index == 1:
                return 'b)'
            elif index == 2:
                return 'c)'
            elif index == 3:
                return 'd)'

          
        print(var(i),option)
    print()

    choose = input('Choose a Answer: ')

    
    if choose == q['Resposta']:
        rights += 1
        
        print('Correct!')
    else:
        
        wrongs += 1
        print('Wrong!')

    

print(f'You got {rights} and {wrongs} mistakes')
