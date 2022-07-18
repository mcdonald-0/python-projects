import random

lives = 9
secret_words = ['panda', 'pizza', 'plaza', 'plate', 'polar', 'pitch', 'price', 'prime', 'pride', 'power']
secret_word = random.choice(secret_words)
clue = ['?', '?', '?', '?', '?']

heart = u'\u2764'

guessed_correctly = False



print(secret_word)
    
print(clue)

def check_guess(secret_word, guess, clue):
    global lives, guessed_correctly, start

    guess_length = len(guess)
    if len(guess) > 1:
        if guess == secret_word:
            guessed_correctly = True
            print('Correctly guessed')
        elif guess in secret_word:
            start = secret_word.index(guess)
            for i in secret_word[start:(len(guess) + 1)]:
                clue[start] = i
                start += 1
            lives -= guess_length
        else:
            lives -= guess_length
    elif guess in secret_word:
        clue[secret_word.index(guess)] = guess
        lives -= guess_length
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
    
