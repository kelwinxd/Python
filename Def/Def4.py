#High Order Function

def Greetings(greet, name):
    return f'{greet}, {name}'

def execute(function, *args):
    return function(*args)


print(execute(Greetings, 'Good morning', 'Kelwin'))

#Closure and Functional functions


def Talking(greet):
    def speech(name):
        return f'{greet}, {name}'
    return speech

cump = Talking('whassup')

for i in ['Kelwin','Gabi','Goku']:
    print(cump(i))