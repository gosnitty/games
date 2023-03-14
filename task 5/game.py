'''
This module contains classes
'''
class Room:
    '''
    a class for item
    '''
    def __init__(self, room):
        '''
        ballroom = Room('ballroom')
        ballroom.name
        ballroom
        '''
        self.room = room
        self.character = None
        self.description = None
        self.lst = []
        self.item = None

    def __str__(self):
        '''
        this function returns str
        '''
        return f'{self.room}'

    def set_description(self, description):
        '''
        this function gives a description
        >>> ballroom = Room('ballroom')
        >>> ballroom.set_description('aaa')
        '''
        self.description = description

    def link_room(self, room, position):
        '''
        links rooms by directions
        >>> ballroom = Room('ballroom')
        >>> ballroom.set_description('description')
        >>> kitchen = Room('Kitchen')
        '''
        self.lst.append([room, position])
        return self.lst

    def set_item(self, item):
        '''
        tgis function sets item in room
        '''
        self.item = item

    def set_character(self, character):
        '''
        this function sets character in room
        '''
        self.character = character

    def get_details(self):
        '''
        this function prints info about the room
        >>> ballroom = Room("ballroom")
        >>> ballroom.set_description("description")
        >>> ballroom.get_details()
        ballroom
        --------------------
        description
        <BLANKLINE>
        '''
        text = self.room + '\n' + '-'*20 + '\n' + self.description + '\n'
        for items in self.lst:
            text += 'The '+ items[0].room +' is '+ items[1] +'\n'
        print(text)

    def get_character(self):
        '''
        this function gets character from room
        '''
        return self.character

    def get_item(self):
        '''
        this function gets item from room
        '''
        return self.item

    def move(self, direction):
        '''
        this function moves to another room
        '''
        for i in self.lst:
            if direction == i[1]:
                return i[0]
        return self

class Character:
    '''
    a class for character
    '''
    defeat_count = 0
    def __init__(self, name, description):
        '''
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.description
        'A smelly zombie'
        '''
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        '''
        this function adds conversation
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        '''
        self.conversation = conversation

    def set_weakness(self, weakness):
        '''
        this function sets weakness of an enemy
        '''
        self.weakness = weakness

    def describe(self):
        '''
        this function describes an enemy
        '''
        print(f'{self.name} is here! \n {self.description}')

    def talk(self):
        '''
        this function returns str with conversation
        '''
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, fight_with):
        '''
        this function fights an enemy with given item
        '''
        if fight_with == self.weakness:
            Character.defeat_count += 1
            print(f'You fend {self.name} with the {fight_with}')
            return True
        print(self.name + ' crushes you, pune adventurer')
        return False

    def get_defeated(self):
        '''
        this function return a number of defeated enemies
        '''
        return Character.defeat_count

class Enemy(Character):
    '''
    sets class Enemy
    '''
    def __init__(self, name, description):
        '''
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.description
        'A smelly zombie'
        '''
        super().__init__(name, description)
class Item:
    '''
    sets class Item
    '''
    def __init__(self, name):
        '''
        book = Item("book")
        book.name
        book
        '''
        self.name = name
        self.description = None

    def get_name(self):
        '''
        this function gets name of an item
        '''
        return self.name

    def set_description(self, description):
        '''
        this function sets a description
        '''
        self.description = description

    def describe(self):
        '''
        this function prints a description
        '''
        print(f'The [{self.name}] is here - {self.description}')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
