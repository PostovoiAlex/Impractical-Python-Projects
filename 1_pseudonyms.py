"""
This script generates funny names
"""

import random
from termcolor import colored

first = (
    'Baby ', 'Bad', 'Big ', 'Bill ', 'Bob ', 'Bowel ', 'Boxelder', 'Bud ',
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy',
    'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab', 'Crapps', 'Dark',
    'Dennis', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
    'Greasy', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', 'Joe', 'Johnny',
    'Lemongrass', 'Lil', 'Longbranch', 'Mergatroid', 'Oil-Сап', 'Oinks', 'Old',
    'Ovaltine', 'Pennywhistle', 'Pitchfork ', 'Potato', 'Pushmeet', 'Rock',
    'Schlomo', 'Scratchensniff', 'Scut', 'Sid', 'Skidmark', 'Slaps', 'Snakes',''
    'Snoobs', 'Snorki', 'Soupcan', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
    'Sweet', 'TeeTee', 'Wheezy', 'Winston', 'Worms'
)

middle = (
    'Oil1', 'News', 'Burps', 'Beenie-Weenie', 'Stinkbug', 'Noises', 'Lite', 'Meat',
    'Skies', 'Clawhammer', 'Jim', 'Pottin Soil', 'Debil', 'Lunch Money', 'Peabody',
    'Scratch', 'Ben', 'Bug', 'Candy', 'The Squirts', 'Sam', 'Tea', 'Joe', 'Jazz Hands',
    'The Big News', 'Grunts', 'Tinkie Winkle'
)

last = (
    'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh',
    'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
    'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins',
    'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bernbo",
    'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck',
    'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
    'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider',
    'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
    'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks'
)

print('Hello, and wellcome to program "Generate fanny names"')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    middle_name = random.choice(middle)

    have_middle_name = random.randint(0, 1)
    print()

    if have_middle_name:
        print(colored(f'{firstName} "{middle_name}" {lastName}', 'red'))
    else:
        print(colored(f'{firstName} {lastName}', 'red'))

    try_again = input(
        '\nYou want try again? \n'
        '(press n if you want close program or press enter if you want to try again ): '
    )

    if try_again.lower() == 'n':
        break

input('Press enter for close')
