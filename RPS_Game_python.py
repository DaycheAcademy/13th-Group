import random

def changInput(*user):
    for i in user:
        if i in ('rock', 'r'):
            return 'rock'
        elif i in ('scissors', 's'):
            return 'scissors'
        elif i in ('paper', 'p'):
            return 'paper'

    return ''


def check_win(pc, user):
    t_Wins = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))

    if (user, pc) in t_Wins:
        return True

selectUser = dict.fromkeys(['s', 'scissors'], 'scissors')
selectUser.update(dict.fromkeys(['r', 'rock'], 'rock'))
selectUser.update(dict.fromkeys(['p', 'paper'], 'paper'))

myList = ['rock', 'paper', 'scissors']

while True:

    countRepeat = input("Enter the number of repetitions of the game or enter (q/quit) to exit:")

    if 'q' in countRepeat.lower().split(' ') or 'quit' in countRepeat.lower().split(' '):
        print("GOODBYE")
        exit()
    if countRepeat.isdigit():
        countWinsPC = 0
        countWinsUser = 0
        countWinsPcAndUser = 0
        checkwhile = int(0)

        while int(countRepeat) >= checkwhile:

            userInput = input("please select either rock(r), paper(p) or scissors(s) (or q/quit to exit) ")
            RandomPc = random.choice(myList)

            if 'q' in countRepeat.lower().split(' ') or 'quit' in countRepeat.lower().split(' '):
                print("GOODBYE")
                exit()
            elif userInput.isdigit():
                continue
            else:
                userInput = userInput.lower().strip().split(' ')
                userInput = changInput(*userInput)
                if userInput == '':
                    print("Please select from limited")
                    continue

                print('\33[36m' + '\nuserInput:{}'.format(userInput), '\nRandomPc:{}'.format(RandomPc))


                if RandomPc == userInput:
                    print("equal to ...")
                    countWinsPcAndUser += 1
                elif check_win(RandomPc, userInput):
                    print("user wins!....")
                    countWinsUser += 1
                elif not check_win(RandomPc, userInput):
                    print("pc wins!...")
                    countWinsPC += 1
                else:
                    print("something went wrong ....")
            print('\33[35m' + '*' * 30)
            print(
                f'\33[31m countWinsPcAndUser: {countWinsPcAndUser} \n\33[32m countWinsPC: {countWinsPC}\n\33[33m countWinsUser: {countWinsUser}')
            print('\33[35m' + '*' * 30)

            checkwhile += 1

            if checkwhile == int(countRepeat):
                if countWinsPC > countWinsUser:
                    print('-'*10, 'Computer won', '-'*10)
                elif countWinsPC < countWinsUser:
                    print('-' * 10, 'User won', '-' * 10)
                else:
                    print('-' * 10, 'The game was tied', '-' * 10)


                while True:

                    checkContinued = input("do you want to continue? [yes/no][y/n]")

                    if checkContinued.strip().lower() in ('n', 'no'):
                        print("----------GOODBYE----------")
                        exit()
                    elif checkContinued.strip().lower() in ('y', 'yes'):
                        break
                    else:
                        print('Selected out of range. Please select again: [yes/no][y/n]')
                        continue
                break


                   #countRepeat = input("Enter the number of repetitions of the game or enter (q/quit) to exit:")

                    #if 'q' in countRepeat.lower().split(' ') or 'quit' in countRepeat.lower().split(' '):
                        #print("----------GOODBYE----------")
                        #exit()