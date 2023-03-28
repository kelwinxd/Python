var = 'Something'

print(f'{var:a^20}')

#Convenção entre programadores para definir uma variável constante 
#é colocar em Maíusculo

VEL_1 = 80


vel = 65
car_place = 90

RADAR_1 = 60
RLOCAL = 100
RADAR_RANGE = 2
# you may use \ to write on another paragraph
vel_car = vel > RADAR_1
car_passed = car_place >= (RLOCAL - RADAR_RANGE) \
    and car_place <= (RLOCAL + RADAR_RANGE)
cited_car = vel_car and car_passed

if vel_car:
    print(f'Your car passed the traffic radar')
if cited_car:
    print(f'Your were cited!')