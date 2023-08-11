letter = set()

while True:
    quetion = input('What year did Brazil become independent?')
    letter.add(quetion)

    if '1822' in letter:
        print('You are Right!')
        break

    print(letter)