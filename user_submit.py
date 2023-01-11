#initial class of 'shoe'
class shoe:
    brand = 'Puma'
    color = 'black'
    size = '13'
    cost = 0#I am not sure that this is the right type,I did see that there is
              #a money module, just wasn't trying to get that deep yet.

#first instance of a child class
class boot(shoe):
    waterproof = True
    style = 'Work'
    material = 'Leather'
    
#second instance of a child class
class flop(shoe):
    ugly = True
    dumbsound = True

    
