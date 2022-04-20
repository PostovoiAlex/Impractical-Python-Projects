"""
Script takes an expression and returns a bar graph
"""

from pprint import pprint


text = input('Please type text: ').replace(' ', '')

schedule = {}
width = 80

key_list = sorted(list(set(text)))

for i in key_list:
    count = text.count(i)
    if count * 6 > width:
        width = count * 6
    schedule.update({i: list(i * count)})
pprint(schedule, width=width)
