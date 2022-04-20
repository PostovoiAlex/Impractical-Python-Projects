"""
This script changes english words to pig latin
"""

consonants_letter = 'BCDFGHJKLMNPQRSTVXZ'
words = ''

while True:
    word = input('Please, enter you word: ')

    if word[0].upper() in consonants_letter:
        words += word[1:] + word[0] + 'ay' + ' '
    else:
        words += word[1:] + 'way' + ' '

    print(words)

    more_words = input(
        'You want add another word?'
        ' (type "n" if you do not want add another word, or press Enter if you want) :'
    )

    if more_words.upper() == 'N':
        break
