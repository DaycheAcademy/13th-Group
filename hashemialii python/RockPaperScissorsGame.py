import random
import getch

print('Welcome to my game, you can play with our bot\nThis is a famous ROCK PAPER SCISSORS game\nENJOY IT!\n')

userAction = ''
computerAction = ''
computerRandom = ['rock', 'paper', 'scissors']
computer = 0
user = 0
score = 0
gameOver = False

while not gameOver:
    if score == 0:
        while True:
            try:
                score = input('Please type in a value for the wining score: ')
            except Exception:
                print("out")
                exit()
            inpSplit = [i.lower() for i in score.split()]
            if 'quit' in inpSplit or 'q' in inpSplit:
                gameOver = True
                break
            if not score.isdigit():
                continue
            else:
                score = int(score)
                if score == 0:
                    continue
                break

    if gameOver:
        break

    print('\n')
    try:
        inp = input('Please select either Rock, Paper, Scissors (or QUIT to exit): ')
    except Exception:
        print("out")
        exit()
    inpSplit = [i.lower() for i in inp.split()]
    if 'quit' in inpSplit or 'q' in inpSplit:
        break
    if len(set(inpSplit).intersection({'r', 's', 'p', 'rock', 'paper', 'scissors'})) > 1:
        print('I did not get your choice, try again!')
        continue
    if 'r' in inpSplit or 'rock' in inpSplit:
        userAction = 'rock'
    elif 'p' in inpSplit or 'paper' in inpSplit:
        userAction = 'paper'
    elif 's' in inpSplit or 'scissors' in inpSplit:
        userAction = 'scissors'
    else:
        userAction = ''
        print('Try again')

    computerAction = random.choice(computerRandom)
    print('\n')
    if computerAction == userAction:

        print('\n' 'Tied! your choice was same as me: {}\nNobody could not take this score!'.format(computerAction))
        print()
        print("""

                =========================================

        """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'rock' and userAction == 'paper':
        user += 1
        print('You are lucky,\nMy choice was: ROCK and your choice was: PAPER')
        print("""

                =========================================

                """)
        print('Computer score is: ', computer, '\nuser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'rock' and userAction == 'scissors':
        computer += 1
        print('I am literally better than you\nmy choice was: ROCK and your choice was: SCISSORS')
        print("""

                =========================================

                        """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'paper' and userAction == 'rock':
        computer += 1
        print('I am literally better than you\nMy choice was: PAPER and your choice was: ROCK')
        print("""

                =========================================

                                """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'paper' and userAction == 'scissors':
        user += 1
        print('You are lucky,\nMy choice was: PAPER and your choice was: SCISSORS')
        print("""

                =========================================

                        """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'scissors' and userAction == 'rock':
        user += 1
        print('You are lucky,\nMy choice was: SCISSORS and your choice was: ROCK')
        print("""

                =========================================

                        """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    elif computerAction == 'scissors' and userAction == 'paper':
        computer += 1
        print('I am literally better than you\nMy choice was: SCISSORS and your choice was: PAPER')
        print("""

                =========================================

                                """)
        print('Computer score is: ', computer, '\nUser score is: ', user)
        print("""

                =========================================

                """)

    if computer == score or user == score:
        while True:
            try:
                inp = input('Do you want to play again? (Yes or No)')
            except Exception:
                print("out")
                exit()
            if inp.isnumeric():
                continue
            inpSplit = [i.lower() for i in inp.split()]
            if 'y' in inpSplit or 'yes' in inpSplit:
                computer = 0
                user = 0
                score = 0
                break
            elif 'n' in inpSplit or 'no' in inpSplit:
                gameOver = True
                break
            else:
                continue

if int(user) > int(computer):
    print('\nBe happy, you won the match')
if int(user) < int(computer):
    print('I told you that I\'m literally better than you')
if int(user) == int(computer):
    print('Tied, you know that you will not win. So, gave up')

print("PRESS ANY KEY TO EXIT")
getch.getch()