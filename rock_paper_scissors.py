import random

def rock_paper_scissors():
    player_one = random.randint(1, 3)
    player_two = random.randint(1, 3)

    if player_one == 1:
        if player_two == 1:
            print('rock DRAWS rock')
        elif player_two == 2:
            print('rock LOSES paper')
        else:
            print('rock BEATS scissors')
    elif player_one == 2:
        if player_two == 1:
            print('paper BEATS rock')
        elif player_two == 2:
            print('paper DRAWS paper')
        else:
            print('paper LOSES scissors')
    else:
        if player_two == 1:
            print('scissors LOSES rock')
        elif player_two == 2:
            print('scissors BEATS paper')
        else:
            print('scissors DRAWS scissors')

rock_paper_scissors()