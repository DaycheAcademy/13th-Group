import random

keywords_game = ['R', 'ROCK', 'S', 'SCISSOR', 'P', 'PAPER']
computer_choices = 'ROCK', 'SCISSOR', 'PAPER'
 
def get_count_win_score():
    while True:
        req = input('🏆 Enter The Winning Score:')
        if req.isdigit():
            break
    return int(req)

def check_user_input(input):
    return True if input.isalpha and input.upper() in keywords_game else False

def quit_game(player_value):
    if 'Q' in player_value or 'quit' in player_value:
        exit()
        
def get_user_input():
    while True:
        req = input('select 📃 Paper, 🪨 Rock, ✂️ SCISSOR or Q to quit >>>: ')
        quit_game(req)
        if check_user_input(req):
            return req



def check_score(player_choice, computer_choice, player_score, computer_score):
    if player_choice == computer_choice:
        print('You and Computer are the same')
    elif player_choice == 'ROCK' or player_choice == 'R':
        if computer_choice == "PAPER":
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 🥴 You lost a Score'.format())
            computer_score += 1

        else:
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 👻 Yeh You got a Score')
            player_score += 1
    elif player_choice == 'PAPER':
        if computer_choice == "SCISSOR":
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 🥴 You lost a Score')
            computer_score += 1
        else:
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 👻 Yeh You got a Score')
            player_score += 1
    elif player_choice == 'SCISSOR':
        if computer_choice == "ROCK":
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 🥴 You lost a Score')
            computer_score += 1
        else:
            print(f'Computer chose {computer_choice} and you chose {player_choice}!!! 👻 Yeh You got a Score')
            player_score += 1

    return player_score, computer_score

def check_play():
     while True:
        req = input("Do you wonna to continue the game? : ")
        if  req.upper() in ['YES', 'Y'] :
            play_game()
            break
        elif req.upper() in ['NO', 'N']:
            exit()

def check_winner(player_score , computer_score):
    if player_score > computer_score :
        print('🥳🍾🎉🥳🍾🎉🥳 CONGRATULATIONS!!! YOU WON 🏆')
        while True:
            want_to_continue = input("Do you wanna to continue the game? : ")
            if 'yes' in want_to_continue:
                player_score = computer_score = 0
                break
            elif 'no' in want_to_continue:
                exit(0)
    else:
        print('😯 OH!!! MAYBE NEXT TIME 😛')
    
def play_game():
    player_score = computer_score = 0
    print('👾👾👾 GOOD LUCK 👾👾👾')
    winning_score_count = get_count_win_score()
    
    while computer_score < winning_score_count and player_score < winning_score_count:
        player_value = get_user_input()
        
        computer_value = ''.join(random.sample(computer_choices, 1))
            
        player_score, computer_score = check_score(player_value.upper(), computer_value, player_score, computer_score)
        
        print(f'🤖 Computer Score: {computer_score}')
        print(f'👤 Player Score: {player_score}')
        
    check_winner(player_score , computer_score)
    check_play()
    
play_game()