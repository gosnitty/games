import my_game

cucu = my_game.Room('КУКУ')
cucu.set_description("Альма-матер - УКУ.")

park = my_game.Room("Стрийський  парк")
park.set_description("Чудовий парк, але в ночі проходять багато загадкових персонажів")

Snopkiv_street = my_game.Room("вул. Снопківська")
Snopkiv_street.set_description("Вулиця ніколи не залишить тебе без пригод, але тут проживає твій друг")

cucu.link_room(park, "вперед")
park.link_room(cucu, "назад")
park.link_room(Snopkiv_street, "направо")
Snopkiv_street.link_room(park, "на ліво")

dave = my_game.Enemy("Жінка", "Дама легкої поведінки напідпитку")
dave.set_conversation("Пива...хочу..")
dave.set_weakness("пиво")
park.set_character(dave)

bomzh = my_game.Enemy("безхатько Валєра", "Безхатько, який любить чіплятись до усіх")
bomzh.set_conversation("ее..куди йдеш..")
bomzh.set_weakness("книжка")
Snopkiv_street.set_character(bomzh)

friend = my_game.Friend('Подруга', 'Одногрупниця, яка повертається з шотів')
friend.set_conversation('Знайшла книжку з алгоритмів, можу віддати')
cucu.set_character(friend)

book = my_game.Item("книжка")
book.set_description("Дуже груба книжка, а основне інформативна.")
friend.set_item(book)

pivo = my_game.Item("пиво")
pivo.set_description("Надпита пляшка ароматного пива покинути у стрийському якимось богословом")
park.set_item(pivo)


# book = my_game.Item("book")
# book.set_description("A really good book entitled 'Knitting for dummies'")
# Snopkiv_street.set_item(book)

current_room = cucu
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    if inhabitant is not None:
        item2 = inhabitant.get_item()
        if item2 is not None:
            item2.describe()
    print('<<<Твої команди: взяти, позбутись, поговорити, вперед, назад, направо, на ліво>>>')
    command = input("> ")
    if command in ["вперед", "назад", "направо", "на ліво"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "поговорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "позбутись":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим саме?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Єєє, ти поборов цю перешкоду")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Вітаю! Ти добрався до дому свого друга")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Ти не переграв опонента, більше ти не потрапиш до свого друга")
                    # print("That's the end of the my_game")
                    dead = True
            else:
                print("Ти не може побороти перешкоду з " + fight_with)
        else:
            print("Тут нічого тобі не загрожує")
    elif command == "взяти":
        if item is not None:
            print("Ти поклав " + item.get_name() + " в шопер")
            backpack.append(item.get_name())
            current_room.set_item(None)
        if item2 is not None:
            print("Ти поклав " + item2.get_name() + " в шопер")
            backpack.append(item2.get_name())
            inhabitant.set_item(None)
        else:
            print("Тут нічого немає")
    else:
        print("Непонятно шо таке " + command)
