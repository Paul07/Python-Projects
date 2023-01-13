class Hidden:#setting the class
    def __init__(self):#instantiating the class
        self._Friday = 13

obj = Hidden()#passing the class into a variable
print(obj._Friday)#printing the variable to the console


class Invisible:
    def __init__(self):
        self.__inVar = 'Reed'
        self.__visVar = 'Richards'

    def reveal(self):#setting a function concatenate the variables above in a string
        print('{} {} is Mr. Fantastic!'.format(self.__inVar, self.__visVar))#the pring function

obj = Invisible()#passing class into variable
obj.reveal()#printing variable to the console

    
    
