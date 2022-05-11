from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')


print('please enter you name')

clear()
print('hellow')