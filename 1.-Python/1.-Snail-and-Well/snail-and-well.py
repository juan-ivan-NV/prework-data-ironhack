print('     The Snail and the Well  ')
well_height = 125
daily_distance = 30
nightly_distance = -20
daily_total = 0
snail_position = 0
snail_under_top = True
days = 0

daily_total = daily_distance + nightly_distance
while snail_under_top:
    snail_position += daily_total 
    days += 1
    if snail_position > well_height:
        snail_under_top = False

print('The snail would escape in '+ str(days) + ' days')
print('')
print()

# Snail bonus

well_height = 125
daily_distance = 30
nightly_distance = -20
daily_total = 0
snail_position = 0
snail_under_top = True
days = 0

advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
advancet_cm =[]
for x in advance_cm:
    daily_total = x + nightly_distance
    if snail_position < well_height:
        advancet_cm.append(daily_total)
        snail_position += daily_total
        days +=1

print('The snail would escape in '+ str(days) + ' days')
print('The total distances are: ',advancet_cm)
advancet_cm.sort()
print('The minimum displacement is: ',advancet_cm[0])
print('The maximum displacement is: ',advancet_cm[-1])
print('The average progres is:', round(snail_position/days,2))

from math import sqrt

def standard_d(advancet_cm):
    suma = 0
    for val in advancet_cm:
        suma += (val - (snail_position/days)) ** 2

    radicando = suma / (days-1)                    #taking the data as a sample of the first list

    return sqrt(radicando)

result = standard_d(advancet_cm)

print('The standard deviation is: {}'.format(result))



    

