def mqtt_update(**kwargs):
    try:
        print('His lastname is : ' + kwargs['lame'])
    except KeyError:
        print("Error: Invalid key in dict")


def another_method(*kids):
    try:
        print('The youngest child is : ' + kids[2])
    except IndexError:
        print('Error: IndexError : Tuple index out of range')


another_method('Tobias', 'beers')
mqtt_update(fname='Tobias', lname='Refsnes')

