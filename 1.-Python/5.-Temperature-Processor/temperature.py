temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
#1 Find the minimum temperature of the day and store it in a variable
min_temp = min(temperatures_C)

#2 Find the maximum temperature of the day and store it in a variable 
max_temp = max(temperatures_C)

#3 List with the temperatures that are greater than or equal to 70ºC. Store it in a variable
temps_gt_70 = [x for x in temperatures_C if x >=70]
sum = 0

for i in temperatures_C:
    sum += i

print(temps_gt_70)

#4 Find the average temperature of the day and store it in a variable.
average_t = sum/len(temperatures_C)
print(average_t)

#5 Replaceing the missing value
temperatures_C = [average_t if (x == 0) else x for x in temperatures_C]
print(temperatures_C)

#6 Converting temperatures to °F
f = lambda x: (x*1.8)+32
temperatures_F = [round(f(x),1) for x in temperatures_C]
print(temperatures_F)

#7 Making a desition
def make_decition(temperatures_C,average_t,temps_gt_70):
    tmps_great_80 = [x for x in temperatures_C if x > 80]
    Yes = 'The cooling sistem needs to be changed'
    if average_t > 65:
        return Yes
    elif len(temps_gt_70) > 4:
        return Yes
    elif len(tmps_great_80) > 1:
        return Yes
    else:
        print('The cooling sistem doesn´t need to be changed') 
    
print(make_decition(temperatures_C,average_t,temps_gt_70))

#Bonus
#1 List - hours with temperature greater than 70°C
temps_gt_70 = [x for x,y in enumerate(temperatures_C) if y > 70]
print(temps_gt_70)

#2 Check 4 consecutive hours greater than 70°C
from itertools import groupby
from operator import itemgetter
for k, g in groupby(enumerate(temps_gt_70), lambda ix : ix[0] - ix[1]):
    if len(list(map(itemgetter(1),g))) > 3:
        condition_1 = True
        print('Yes there are 4 consecutive hours')

#3 Desition
def make_decition2(condition_1,temperatures_C,average_t):
    ok = 'The Cooling sistem needs to be changed'
    tmps_great_80 = [x for x in temperatures_C if x > 80]
    if condition_1 == True:
        return ok
    elif average_t > 65:
        return ok
    elif len(tmps_great_80) > 1:
        return ok
    else:
        print('The cooling sistem doesn´t need to be changed')
print(make_decition2(condition_1,temperatures_C,average_t))

#4 Average values in °F and °C
sum_C = 0
for i in temperatures_C:
    sum_C +=i
average_t_C = round((sum_C / len(temperatures_C)),1)

sum_F = 0
for i in temperatures_F:
    sum_F +=i
average_t_F = round((sum_F / len(temperatures_F)),1)

print('The relation between both averages {} C and {} F is the formula in step 6.'.format(average_t_C,average_t_F))

#5 STD DEV °F and °C
from math import sqrt
def standard_d(list_g,averag):
    acum = 0
    for i in list_g:
        acum += (i - averag)**2
    return sqrt(acum/len(list_g))

dev_C = round((standard_d(temperatures_C,average_t_C)),1)
dev_F = round((standard_d(temperatures_F,average_t_F)),1)

print('The standard dev {} °F is bigger than {} °C because the values in °F are more spread'.format(dev_F,dev_C))