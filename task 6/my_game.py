class Room:
    def __init__(self, room):
        self.room = room
        self.character = None
        self.description = None
        self.lst = []
        self.item = None

    def __str__(self):
        return f'{self.room}'

    def set_description(self, description):
        self.description = description

    def link_room(self, room, position):
        self.lst.append([room, position])
        return self.lst

    def set_item(self, item):
        self.item = item

    def set_character(self, character):
        self.character = character

    def get_details(self):
        text = (self.room + '\n' + '-'*20 + '\n' + self.description + '\n')
        for items in self.lst:
            text += items[0].room +' є '+ items[1] +'\n'
        print(text)

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        for i in self.lst:
            if direction == i[1]:
                return i[0]
        return self

class Character:
    defeat_count = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(f'{self.name} тут! \n {self.description}')

    def talk(self):
        print(f'[{self.name} каже]: {self.conversation}')

    def fight(self, fight_with):
        if fight_with == self.weakness:
            Character.defeat_count += 1
            print('Ти пройшлов цю перешкоду')
            return True
        print('Ти не впорався(')
        return False

    def get_defeated(self):
        return Character.defeat_count

    def get_item(self):
        return None

class Enemy(Character):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'[{self.name}] тут - {self.description}')

class Friend(Character):
    def __init__(self, name, description):
        self.item = None
        super().__init__(name, description)

    def talk(self):
        print(f'[{self.name} каже]: {self.conversation}')

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item
