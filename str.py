year = 2016
event = 'Referendum'
f = f'Results of the {year} {event}'
print(f)


# difference of repr() and str()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

# string format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

def testStringFormat():
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

testStringFormat()

