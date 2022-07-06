import time

score = 0

print('This is my modified version of the guessing game🤭')

username = input('Before we start, what\'s your name... ')
print(f'Thank you {username}, You can start the game!')


def check_answer(user_answer, answer, alternative_answer):
    if user_answer.lower() == answer or user_answer.lower() == alternative_answer:
        score += 1
        still_guessing = True
        print('Correct')
    else:
        print('Incorrect')

question1 = input('Can a penguin fly? ')
check_answer(question1, 'no', 'nah')
question2 = input('A group of ravens is called? ')
check_answer(question2, 'a conspiracy', 'conspiracy')
question3 = input('What\'s your name? ')
check_answer(question3, username, username)
question4 = input('What is the current time? ')
check_answer(question4, time.strftime('%H:%M'), time.strftime('%I:%M%p').lower())

print(f'Congratulations on finishing the game {username}, Your score is {score}')

