#initial class of 'shoe'
class shoe:
    brand = ''
    color = ''
    size = ''
    cost = int#I am not sure that this is the right type,I did see that there is
              #a money module, just wasn't trying to get that deep yet.

#first instance of a child class
class boot(shoe):
    waterproof = True
    style = ''
    material = ''
    
#second instance of a child class
class flop(shoe):
    ugly = True
    dumbsound = True

    
