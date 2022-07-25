import random

lives = 9
secret_words = ['panda', 'pizza', 'plaza', 'plate', 'polar', 'pitch', 'price', 'prime', 'pride', 'power']
secret_word = random.choice(secret_words)
clue = ['?', '?', '?', '?', '?']

heart = u'\u2764'

guessed_correctly = False
