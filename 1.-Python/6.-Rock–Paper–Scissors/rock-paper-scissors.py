print(' This game is rock, paper or scissors. \n')
#1 Import the choice function of the
import random

#2 List 3 possible options
gestures = ['Rock','Paper','Scissors']

#3 Variable to store the maxomum number of rounds
n_rounds = 3

#4 Variable to store the number of rounds must be wined to be the winner
rounds_to_win = 2

#5 Variables to store number of wins
cpu_score  = 0
player_score = 0

#6 Function that randomly returns one of 3 gesture options

def cpu_choice(gestures):
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        return gestures [0]
    elif comp_choice == 2:
        return gestures [1]
    else: 
        return gestures [2]
#cpu = cpu_choice(gestures)
#print(cpu)

7# User´s choice

def usr_choi(gestures):
    print('Enter the number of your choice: \n 1: %s \n 2: %s \n 3.- %s '%(gestures[0], gestures[1], gestures[2]))
    user_choice = int(input(' Number: '))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Enter a valid number: '))

    if user_choice == 1:
        return gestures [0]
    if user_choice == 2:
        return gestures [1]
    if user_choice == 3:
        return gestures [2]
#user = usr_choi(gestures)
#print(user)

#8 Definnig who won
def round(user,cpu,gestures):
    if user == cpu:
        return 0
    elif user == gestures [0] and cpu == gestures [1]:
        return 1
    elif user == gestures [0] and cpu == gestures [2]:
        return 2
    elif user == gestures [1] and cpu == gestures [2]:
        return 1
    elif user == gestures [1] and cpu == gestures [0]:
        return 2
    elif user == gestures [2] and cpu == gestures [0]:
        return 1
    elif user == gestures [2] and cpu == gestures [1]:
        return 2
#print(round(user,cpu,gestures))

#9 Function winner match
def round_winner(round,user,cpu):
    print('The computer´s choice is {} and your choice is {}'.format(cpu,user))
    if round(user,cpu,gestures) == 0:
        print('Round tie')
    elif round(user,cpu,gestures) == 1:
        print('The computer wins this round')
    elif round(user,cpu,gestures) == 2:
        print('You win')
    else:
        pass
#print(round_winner(round,user,cpu))

#10 Execution of the game

actual_round = 0

while actual_round < n_rounds:
    actual_round += 1
    cpu_choice(gestures)
    cpu = cpu_choice(gestures)
    print(cpu)
    usr_choi(gestures)
    user = usr_choi(gestures)
    print(user)
    round(user,cpu,gestures)
    print(round(user,cpu,gestures))
    round_winner(round,user,cpu)
    print(round_winner(round,user,cpu))

    if round(user,cpu,gestures) == 1:
        cpu_score +=1
    elif round(user,cpu,gestures) == 2:
        player_score +=1
    else:
        pass
# 11 who is the winner of the match
    if player_score == rounds_to_win:
        print('you win the game')
        break
    elif cpu_score == rounds_to_win:
        print('The computer wins the game')
        break

    




    




