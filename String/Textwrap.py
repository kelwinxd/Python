import textwrap
n, num = input(), int(input())

def formating(n,num):
    textwrap.wrap(n,num)
    return print(textwrap.fill(n,num))

formating(n,num)