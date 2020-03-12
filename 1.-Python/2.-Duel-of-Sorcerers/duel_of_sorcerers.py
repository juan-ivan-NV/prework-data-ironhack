#1 Two variables to store the spells and one more to store the spells
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

spells = []
#2 Two variables to store the voctories
gandalf_wins = 0
saruman_wins = 0
#3 Counting the number of wins
for i in range(len(gandalf)):
    spells.append(gandalf[i] - saruman[i])
    if gandalf[i] > saruman[i]:
        gandalf_wins +=1
    else:
        saruman_wins +=1
#4 who won the battle based on the total number of victories
if gandalf_wins > saruman_wins:
    print('Gandalf is the winner')
elif gandalf_wins == saruman_wins:
    print('It is a tie')
else:
    print('Saruman is the winner')

print('Gandalf wins: ',gandalf_wins)
print('Saruman wins: ',saruman_wins)
print('Spell scores: ',spells)
print('\n\n')



# Bonus
#1 New variables
POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

#2 Gandalf and saruman wins variables
gan_wins_row = 0
sar_wins_row = 0
gandalf_average = 0
gandalft=0
saruman_average = 0
sarumant = 0

#3 Variables Gandalf and Saruman power
gandalf_power = []
saruman_power = []
spells = []

# Asigning values to each spell string on both lists 
for i in gandalf:
    for key,value in POWER.items():
        if i == key:
            gandalf_power.append(value)

for i in saruman:
    for key,value in POWER.items():
        if i == key:
            saruman_power.append(value)

print('Gandalf spell scores: ',gandalf_power)
print('Saruman spell scores: ',saruman_power)

#4 Counting sorceres wins
for i in range(len(gandalf_power)):
    spells.append(gandalf_power[i] - saruman_power[i])
    gandalft += gandalf_power[i]
    sarumant += saruman_power[i]
print('Spells scores differences: ',spells)
    
# Code for 3 wins in a row
x = 0
for i in spells:
    x =+ 1
    if i > 0:
        gan_wins_row +=1
        if gan_wins_row >= 1:
            sar_wins_row = 0  
    elif i < 0:
        sar_wins_row +=1
        if sar_wins_row >= 1:
            gan_wins_row = 0
    else:
        pass

    if gan_wins_row == 3:
        print('gandalf wins')
        break
    elif sar_wins_row == 3:
        print('saruman wins')
        break
    elif x == len(spells):
        print('Tie')
        break



#5 Average spell power
gandalf_average = (gandalft/len(gandalf_power))
saruman_average = (sarumant/len(saruman_power))

print('Gandalf average power: ',gandalf_average)
print('Saruman average power: ',saruman_average)

#6 Standar deviation
from math import sqrt

def standard_d(gandalf_power):
    sum = 0
    for val in gandalf_power:
        sum = (val - gandalf_average) ** 2

    radicando = sum / (len(gandalf_power))

    return sqrt(radicando)


def standard_d(saruman_power):
    sum = 0
    for val in saruman_power:
        sum = (val - saruman_average) ** 2

    radicando = sum / (len(saruman_power))

    return sqrt(radicando)

print('Gandalf´s standar deviation of spell power:',standard_d(gandalf_power))
print('Saruman´s standar deviation of spell power:',standard_d(saruman_power))



'''spells = [-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1]
gandalf_v = []
saruman_v = []
x = 0
for i in spells:
    x +=1
    if i == 1:
        gandalf_v.append(1)
        print(gandalf_v)
        if len(gandalf_v) >= 1:
            saruman_v = [] 
    elif i == -1:
        saruman_v.append(-1)
        print(saruman_v)
        if len(saruman_v) >= 1:
            gandalf_v = []
    else:
        pass

    print('g,s',len(gandalf_v),len(saruman_v))
    if gandalf_v.count(1) == 3:
        print('gandalf wins')
        break
    elif saruman_v.count(-1) == 3:
        print('saruman wins')
        break
    elif x == len(spells):
        print('Tie')
        break

    
print(gandalf_v)
print(saruman_v)'''

