def start(nice=0,mean=0,name=''):
    #Get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not
        If it is, get the user's name
        If it is not, then thank the player
        for playing and continue
    """
    #If we do not have the user's name already
    #then they are a new player and we need to get it
    if name !='':
        print('\nThank you for playing again, {}'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nWhat is your name? \n>>> ').capitalize()
                if name != '':
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                    print('but at the end of the game your fate \nwill be sealed by your actions.')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice \nor mean (N/M)   \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger grins and walks away...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \ndisgustedly and storms off...')
            mean = (mean + 1)
            stop = False
        score(nice, mean, name) #pass the 3 variables to score

def show_score(nice,mean,name):
    print('\n{}, your current total: \n({}, Nice)and ({}, Mean)'.format(name,nice,mean))

def score(nice,mean,name):
    #score function is passed the values stored in the 3 variables.
    if nice > 2: #if the condition is vaild, call win function and pass in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function and pass in the variables so it can use them
        lose(nice,mean,name)
    else:        #else call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #sub the {} wildcards with our variable values
    print('\nWay to go {}! You win! \nYou\'re a hero and you\'ve \nmade lots of friends along the way!'.format(name))
    #call again function and pass in the variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #sub the {} wildcards with our variable values
    print("\nToo bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone! Congrats on nothing!!!!".format(name))
    #call again function and pass in the variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>").lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nSo sad, do please come back soon!')
            stop = False
            quit()
        else:
            print('\nEnter ( Y ) for "YES", ( N ) for "NO": \n>>> ')

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #The name variable is not reset because the same user has chosen to play again
    start(nice,mean,name)




if __name__ == "__main__":
    start()
