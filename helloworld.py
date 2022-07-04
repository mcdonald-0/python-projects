user_score = 0
user_trial_count = 5
questions_answered = 0
print('This is a "Guess the Animal" game...!')
questions = [
    'Which bear lives in the north pole?',
    'Which is the fastest land animal?',
    'Which is the largest animal?',
    ]
answers = [
    'polar bear',
    'cheetah',
    'blue whale',
    ]
i = 0
while user_trial_count > 0 and questions_answered != 3:
    for question in questions:
        print(f'user trial = {user_trial_count}')
        user_answer = input(f'{question} ')
        
        while user_answer != answers[i] and user_trial_count == 1:
            user_trial_count -= 1
            print('Sorry, wrong answer. Try again ')
            user_answer = input(f'{question} ')
            if user_trial_count == 2:
                print(f'The correct answer is {answers[1]}')
            if user_answer == answers[i]:
                break

            
        if user_answer == answers[i]:
            user_score += 1

        i += 1
        user_trial_count -= 1
    break
