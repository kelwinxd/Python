weight = int(input('Enter Your Weight in kilogram: '))
height = float(input('Enter your Height in cm: '))
result = 0

def Icm():
    result = weight / (height*height)
    print(f'Your IMC is around {int(round(result))}')

Icm()

