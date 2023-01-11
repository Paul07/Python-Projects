#parent class
class Parent:
    name = 'Doug'
    email = 'doug@dougmail.com'
    passcode = 'KingDoug'


    def signIn(self):
        sign_name = input('Please tell us your name: ')
        sign_email = input('Please enter your email: ')
        sign_passcode = input('Please enter your password: ')
        if (sign_email == self.email and sign_passcode == self.passcode):
            print('Nice to see you {}'.format(sign_name))
        else:
            print('You\'re not {}'.format(sign_name))

#first child class
class Kid1(Parent):
    nickname = 'Kiddo'#replaces name in the method
    age = 7
    email = 'kid1@dougmail.com'
    passcode = 'Turtles'

    def signIn(self):
        sign_nickname = input('Please tell us your nickname: ')
        sign_email = input('Please enter your email: ')
        sign_passcode = input('Please enter your password: ')
        if (sign_email == self.email and sign_passcode == self.passcode):
            print('Nice to see you {}'.format(sign_nickname))
        else:
            print('I don\'t think you are really {}'.format(sign_nickname))

#second child class
class Kid2(Parent):
    name = 'Grumpy'
    phoneNumber = '123-456-7890'#replaces email in the method
    hasFriends = True
    passcode = 'k-pop'

    def signIn(self):
        sign_nickname = input('Please tell us your name: ')
        sign_phoneNumber = input('Please enter your phone number: ')
        sign_passcode = input('Please enter your password: ')
        if (sign_phoneNumber == self.phoneNumber and sign_passcode == self.passcode):
            print('Nice to see you {}'.format(sign_nickname))
        else:
            print('WHAT!!! NO WAY YOU ARE {}'.format(sign_nickname))


#runs all 3 back to back to back
if __name__ == '__main__':
    Doug = Parent()
    Doug.signIn()

    Kiddo = Kid1()
    Kiddo.signIn()

    Grumpy = Kid2()
    Grumpy.signIn()
