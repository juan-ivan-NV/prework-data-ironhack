print(' This game is rock, paper or scissors. \n')
import random
gestures = ['Rock','Paper','Scissors']
cpu_score  = 0
player_score = 0
actual_round = 0

print('Decide the rounds of the match, Enter a odd number. ')
n_rounds = int(input('Number: '))
while n_rounds % 2 == 0 or n_rounds == 0:
    n_rounds = int(input('Enter a valid number: '))

rounds_to_win = (n_rounds/2) + 0.5

while True:
    
    actual_round += 1
    if actual_round > n_rounds:
        print('\none more round to designate a champion')

    print('\nRound number {}'.format(actual_round))
    def cpu_choice(gestures):
        comp_choice = random.randint(1,3)
        if comp_choice == 1:
            return gestures [0]
        elif comp_choice == 2:
            return gestures [1]
        else: 
            return gestures [2]
    cpu = cpu_choice(gestures)
    
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
    user = usr_choi(gestures)
    print(user)
    
    def round(user,cpu,gestures):
        if user == cpu:
            return 0
        elif (user == gestures [0] and cpu == gestures [1]) or (user == gestures [1] and cpu == gestures [2]):
            return 1
        elif (user == gestures [0] and cpu == gestures [2]) or (user == gestures [1] and cpu == gestures [0]):
            return 2
        elif user == gestures [2] and cpu == gestures [0]:
            return 1
        elif user == gestures [2] and cpu == gestures [1]:
            return 2
    
    def round_winner(round,user,cpu):
        print('\nThe computer´s choice is {} and your choice is {}'.format(cpu,user))
        if round(user,cpu,gestures) == 0:
            print('Round tie')
        elif round(user,cpu,gestures) == 1:
            print('The computer wins this round')
        elif round(user,cpu,gestures) == 2:
            print('You win')
        else:
            pass
    print(round_winner(round,user,cpu))

    if round(user,cpu,gestures) == 1:
        cpu_score +=1
    elif round(user,cpu,gestures) == 2:
        player_score +=1
    else:
        pass
    
    if player_score == rounds_to_win:
        print('\nyou win the game')
        break
    elif cpu_score == rounds_to_win:
        print('\nThe computer wins the game')
        break