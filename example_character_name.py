import htlib
from htlib.basicinfo import *

pony = CharEntity('Cydie', 'unicorn', 'white wizard')

print('This is', pony.name + '\'s info:')
print('Name:', pony.name)
print('Race:', pony.race)
print('Type:', pony.type)

input('\nPress enter to continue.\n')

pony_friends = [CharEntity('Sequoia', 'unicorn', 'black wizard'), CharEntity('Cappie', 'unicorn', 'librarian'),
            CharEntity('Natalie', 'pegasus', 'zoo-keeper')]

print('These are', pony.name + '\'s friends:')

for pone in pony_friends:
    print('Name:', pone.name)
    print('Race:', pone.race)
    print('Type:', pone.type)
    print('------')

input('\nPress enter to continue.')

print('\nThis is Cydie\'s entity type:')
print('Entity:', pony.entity)
