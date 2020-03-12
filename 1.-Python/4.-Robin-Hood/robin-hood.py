points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

repeated = []
unique = []

for x in points:
    if x not in unique:
        unique.append(x)
    else:
        if x not in repeated:
            repeated.append(x)
            
print('Interception points:', repeated)

quadrant_1 = 0
quadrant_2 = 0
quadrant_3 = 0
quadrant_4 = 0
any_quadrant = 0

for x,y in points:
    if x > 0 and y > 0:
        quadrant_1 += 1
    elif x < 0 and y > 0:
        quadrant_2 += 1
    elif x < 0 and y < 0:
        quadrant_3 += 1
    elif x > 0 and y < 0:
        quadrant_4 += 1
    else:
        any_quadrant += 1

print('Quadrant 1 = {}, Quadrant 2 = {}, Quadrant 3 = {}, Quadrant 4 = {}, Any quadrant = {} '.format(quadrant_1,quadrant_2,quadrant_3,quadrant_4, any_quadrant))

import math
p1 = [0,0]

distances = []
closest_p = []
out_r9 = []
num_out_r9 = 0

for i in points:
    distance = math.sqrt(((p1[0]-i[0])**2)+((p1[1]-i[1])**2))
    distances.append(distance)
for i in points:
    if math.sqrt(((p1[0]-i[0])**2)+((p1[1]-i[1])**2)) == min(distances):
        closest_p.append(i)
    elif math.sqrt(((p1[0]-i[0])**2)+((p1[1]-i[1])**2)) > 9:
        out_r9.append(i)
        num_out_r9 += 1



print('The closest point to the center is / are: ',closest_p )
print('Points out of target with radius 9 are: {} with coordinates {}'.format(num_out_r9,out_r9))
    
    
