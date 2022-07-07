import time

"--------------------------------- GAME LOGIC --------------------------------------"

def check_answer(user_answer, answer, alternative_answer):
    global score
    attempt = 0
    still_guessing = True
    while still_guessing and attempt < 3:
        if user_answer.lower() == answer or user_answer.lower() == alternative_answer:
            print('Correct')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 3:
                user_answer = input('Incorrect, Try again ')
                attempt += 1
                
    if attempt == 3:
        print(f'The correct answer is {answer}')

def check_username(user_answer, answer):
    global score
    if user_answer == answer:
        score += 1
        print('That\'s corect!')
    else:
        print('It\'s a shame you can\'t remember your own username')

"-------------------------------- GAME STARTS -------------------------------------"

score = 0

print('This is my modified version of the guessing game🤭')

username = input('Before we start, what\'s your name... ')
print(f'Thank you {username}, You can start the game!')
         
# If you want to ask a question, you put the question and call the function just like this
question1 = input('Can a penguin fly? ')
check_answer(question1, 'no', 'nah')
question2 = input('A group of ravens is called? ')
check_answer(question2, 'a conspiracy', 'conspiracy')
question3 = input('What\'s your name? ')
check_username(question3, username)
question4 = input('What is the current time? \n (PS: Write the time in this format "13:10" or "01:13pm") ')
check_answer(question4, time.strftime('%H:%M'), time.strftime('%I:%M%p').lower())
question5 = input('Which one of these is a fish? \n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C or D ')
check_answer(question5, 'c', '3')
question6 = input('Are bat\'s mammals. True or False? ')
check_answer(question6, 'true', 'yes')

if score == 18:
    print(f'Congratulations on finishing the game {username},\n Your score was perfect, {score} of 18')
elif score > 12:
    print(f'Congratulations on finishing the game {username},\n Your score was quite good, {score} of 18')
elif score > 6:
    print(f'Although your score was not quite good, \n Congratulations on finishing the game {username}, you scored {score} of 18')
else:
    print(f'Your score was not good {username}! you scored {score} of 18')


"----------------------------- FINAL COMMENTS ------------------------------------"

'''
This is my tempoary final edit on this game. Later in the future i may add a random functionality where the questions is
gotten from a website at random and the score can be saved in a file so if the user's previous score was better, it would
say so. Also i would build like a gui for this game because this is quite old fashioned.
'''


















