import random

print("This is a sample TicTacToe board enter spot number accortding to this board.")
print("When you enter number it change into your turn value 'x' or 'o'.")

samplboard = {
    '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9'
}


def sampleBoardPrint():
    print(samplboard['1'] + ' | ' + samplboard['2'] + ' | ' + samplboard['3'])
    print('---------');
    print(samplboard['4'] + ' | ' + samplboard['5'] + ' | ' + samplboard['6'])
    print('---------');
    print(samplboard['7'] + ' | ' + samplboard['8'] + ' | ' + samplboard['9'])


sampleBoardPrint()
print()
print("ENJOY THE GAME.......")
print()

theboard = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}


def initializeboard():
    for i in theboard:
        theboard[i] = ' '


def printBoard():
    print(theboard['1'] + ' | ' + theboard['2'] + ' | ' + theboard['3'])
    print('---------');
    print(theboard['4'] + ' | ' + theboard['5'] + ' | ' + theboard['6'])
    print('---------');
    print(theboard['7'] + ' | ' + theboard['8'] + ' | ' + theboard['9'])


def game():
    k = 1
    count = 0

    while count < 9:
        printBoard()
        print(count)
        if k == 1:
            move = int(input("YOUR TURN...."))
            move = str(move)

            if theboard[move] == ' ':
                theboard[move] = 'x'
                count += 1
            else:
                print("THIS SPOT IS FILLED ENTER OTHER NUMBER")
                continue

            k = 0

        elif k == 0:
            print("COMPUTER'S TURN")
            move = random.randint(1, 9)
            move = str(move)

            if theboard[move] == ' ':
                theboard[move] = 'o'
                count += 1
            else:
                print("THIS SPOT IS FILLED ENTER OTHER NUMBER")
                continue

            k = 1

        if count >= 5:
            if theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                if theboard['1'] == 'x':
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                if theboard['4'] == 'x':
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                if theboard['7'] == 'x':
                    print("***********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                if theboard['1'] == 'x':
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                if theboard['3'] == 'x':
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                if theboard['3'] == 'x':
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                if (theboard['2'] == 'x'):
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                if (theboard['1'] == 'x'):
                    print("**********YOU ARE WINNER**********")
                else:
                    print("**********COMPUTER IS WINNER**********")

                break

    printBoard()

    if count == 9:
        print("IT'S A TIE.....")
    print("YOU WANT TO PLAY AGAIN...?")
    print("Enter 1 for Yes")
    print("Enter 2 for No")
    s = int(input())

    if s == 1:
        initializeboard()
        game()
    else:
        return


if__name__ = '__main__'
game()
