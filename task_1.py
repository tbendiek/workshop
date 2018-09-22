name = input('What is your name?')
print(f'Welcome to the dungeon {name}!')
print('Do you go through door 1 or door 2?')

door = input('> ')
def function_else():
    print('Try again!')

if door == '1':
    print('There is a nice vampire asking you if you enjoy life.')
    print('What do you do?')
    print('1. Smile and nod')
    print('2. Scream and run')

    vampire = input('> ')

    if vampire == '1':
        print(f'Congratulations {name}, you found a new friend!')
    elif vampire == '2':
        print(f'Sorry {name}, the vampire is faster. You become a dinner.')
    else:
        print('You are not so good with numbers, are you?')
elif door == '2':
    print(f'Ups {name}, now got trapped')
    print('Do you need help?')
    print('1. Yes, please!')
    print('2. No, thx.')

    trapped = input('> ' )

    if trapped == '1':
        print('Just turn around and leave.')
    elif trapped == '2':
        print('ok, have a good night')
    else:
        print('Don''t cry, just write HELP!')
        last_answer = input()
        if last_answer == 'HELP':
            print('Great we will help you soon!')
        else:
            print('Sorry, Game Over')
else:
    print('You are not so good with number, are you?')
    function_else()

