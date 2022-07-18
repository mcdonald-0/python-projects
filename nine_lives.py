import random

lives = 9
secret_words = ['panda', 'pizza', 'plaza', 'plate', 'polar', 'pitch', 'price', 'prime', 'pride', 'power']
secret_word = random.choice(secret_words)
clue = ['?', '?', '?', '?', '?']

heart = u'\u2764'

guessed_correctly = False



print(secret_word)


start = 0
for i in secret_word:
    clue[start] = i
    start += 1

print(clue)

def check_guess(secret_word, guess, clue):
    global lives, guessed_correctly

    guess_length = len(guess)
    if guess == secret_word:
        guessed_correctly = True
        print('Correctly guessed')
    else:
        lives -= guess_length


while True:
    if lives > 0 and guessed_correctly == False:
        print(clue)
        print(f'Lives left: {lives * heart}')
        guess = input('Guess a letter or the whole word: ').lower()
        

        check_guess(secret_word, guess, clue)
    elif lives == 0 or guessed_correctly == True:
        if lives == 0:
            print('You loose...')
        elif guessed_correctly == True:            
            break
    else:
        print('You mistyped')
        break
    
