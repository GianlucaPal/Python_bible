films = {
    'Finding Dory':[3,5],
    'Bourne':[18,5],
    'Tarzan':[15,5],
    'Ghost Busters':[12,5]
    }

while True:
    
    choice = input('What film would you like to watch?:').strip().title()

    if choice in films:
        age = int(input('How old are you?:').strip())

        #check users age
        if age >=films[choice][1]:
            #check enough seats
            numSeats = films[choice][1]

            if numSeats > 0:
                print('Enjoy your film')
                films[choice][1] = films[choice][1]-1
            else:
                print('sorry, we are sold out')
        else:
            print('You aree underaged, sorry')
    else:
        print('we do not have that film')
