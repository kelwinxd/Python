n = int(input().strip())

def compare():
    if (n % 2 == 0 and ((2 <= n <= 5) or (n > 20))):
        print('Not Weird')
    elif (n % 2 == 0 and 6 <= n <= 20) or not (n % 2 == 0):
        print('weird')

compare()