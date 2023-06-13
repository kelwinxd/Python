#create a function that duplicate, triple and quatriple a number

def multi(multiply):
    def count(number):
        return number * multiply
    return count

duplicate = multi(2)
triple = multi(3)
quatriple = multi(4)

num = int(input('type a number to duplicate: '))

print(triple(num))



      

