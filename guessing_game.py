def check_answer(guess, answer):
    global score
    can_guess = True
    attempt = 0
    while can_guess and attempt < 3:
            
        if guess.lower() == answer.lower():
            score += 1
            print('Correct answer!')
            can_guess = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again ')
            attempt += 1

    if attempt == 3:
        print(f'The correct answer is {answer}')


score = 0
        
print('This is a "Guess the Animal" game...!')

question_1 = input('Which bear lives in the north pole? ')
check_answer(question_1, 'polar bear')
question_2 = input('Which is the fastest land animal? ')
check_answer(question_2, 'cheetah')
question_3 = input('Which is the largest animal? ')
check_answer(question_3, 'blue whale')

print(f'Your score is {score} out of 3')


