'''\
This is the class for creating any entity character.
As long as it's alive and healthy, it will move and do some other stuff!
'''

_EntityList = ('NoneEn', 'PonyEn', 'VehicleEn', 'OtherEn')

class Entity:
    global _EntityList

    '''Base object for any entity type.'''
    def __init__(self, name, entity):
        '''\
        name :The entity name.
        entity :The entity type.
        '''

        self.name = name

        if entity in _EntityList:
            self.entity = entity
        else:
            raise EntityError("{} doesn\'t exist or its cases are wrong.".format(entity))

class CharEntity(Entity):
    '''Character Entity. The child of the Entity type class'''

    char_race = ('Earth Pony', 'Unicorn', 'Pegasus')

    def __init__(self, name, race, type='None', ignoreerror=False):
        '''\
        Create the CharEntity object, with 3 required parameters.
        name :The name of the character of course.
        race :The race/species of the character.
        type :The job or profession of the character. By default, 'None' is used as if they're freelancers.
        ignoreerror :Whether or not to raise an InvalidRaceError.
        '''
        Entity.__init__(self, name, 'PonyEn')

        if race.title() in CharEntity.char_race:
            self.race = race.title()
        else:
            if ignoreerror:
                self.race = 'N/A'
            else:
                raise InvalidRaceError(race.title() + ' doesn\'t exist.')

        self.type = type.title()

# The exceptions for this class

class InvalidRaceError(Exception):
    '''Raise an InvalidRaceError if such race doesn\'t exist in the database.'''
    def __init__(self, errmsg):
        Exception.__init__(self, errmsg)
        self.invalidrace = invalidrace

class EntityError(Exception):
    '''Raise an EntityError if it doesn't exist or it's not spelt exactly on the __EntityList tuple.'''
    def __init__(self, errmsg):
        Exception.__init__(self, errmsg)
