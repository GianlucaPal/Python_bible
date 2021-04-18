knownUsers = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

print(len(knownUsers))

while True:
    print('Hi! my name is Travis')
    name = input('What is your name?: ').strip().capitalize()

    if name in knownUsers:
        print('Hello {}'.format(name))
        remove = input('would you like to be remove from the list (y/n)').strip.lower()

        if  remove == 'y':
            knownUsers.remove(name)
        elif remove == 'n':
            print('no worries, i didnt want you to leave anyways')
    else:
        print('we have not met you yet {}'.format(name))
        add = input('would you like to be added to the list (y/n)').strip().lower()
        if add == 'y':
            knownUsers.append(name)
        elif add == 'n':
            print('no worries, see you around')
