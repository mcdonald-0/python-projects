import random
import string

punctuation = string.punctuation 
adjectives = ['sleepy', 'big', 'small', 'old', 'young', 'preety', 'alert', 'perfect', 'old', 'smart', 'easy', 'hot', 'cute', 'hard', 'busy', 'safe', 'impossible', 'dirty', 'possible']
nouns = ['car', 'adam', 'cat', 'london', 'shoemaker', 'airpod', 'industry', 'austria', 'vaccum', 'eraser', 'room', 'rat', 'restaurant', 'phone', 'canada', 'seoul', 'refrigirator']

password = f'{random.randrange(0, 100)}{random.choice(adjectives)}{random.choice(punctuation)}{random.choice(nouns)}'

print('\
  --------------------------------- Welcome to McDonald\'s random password generator! ---------------------------------\
')

print('''
    This program generates a really safe password for your various accounts, ranging from social media accounts, \
to your phone passwords, this is the right application for you! \n Note: The password generated would take a hacker \
over a thousand years to crack and no one's ever lived that long...
    --------------------------------------- McDonald's password generator 1.0 ---------------------------------------
''')

print(f'''\
                                    ************************************************
                                       ******************************************
                                           **********************************
                                                ************************
                                                      **********
                                        Your password is -- {password} --
                                                      **********
                                               ************************
                                           **********************************
                                      ******************************************
                                    ************************************************            
\
''')
while True:
    user_input = input('                                      Do you require a stronger password... ').lower()
    if user_input == 'yes' or user_input == 'yay' or user_input == 'yeah' or user_input == '0':
        password = f'{random.randrange(0, 100)}{random.choice(adjectives)}{random.choice(punctuation)}{random.choice(nouns)}'
        print(f'''\
                                    ************************************************
                                       ******************************************
                                           **********************************
                                                ************************
                                                      **********
                                        Your new password is -- {password} --
                                                      **********
                                               ************************
                                           **********************************
                                      ******************************************
                                    ************************************************            
\
''')
    elif user_input == 'no' or user_input == 'nay' or user_input == 'nah' or user_input == '1':
        print(f'''\
                                    ************************************************
                                       ******************************************
                                           **********************************
                                                ************************
                                                      **********
         Hahaha... You have chosen "{password}", the strongest password in history... Farewell my friend...
                                                      **********
                                               ************************
                                           **********************************
                                      ******************************************
                                    ************************************************            
\
''')
        break
    else:
        print('                                 It seems like you mistyped your request... Try again')








