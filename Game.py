from Hero import Hero, Enemy, Equipment
import sys, os
from time import time as t
from time import sleep as s


def show_map(map_list):
    os.system("CLS")
    for key, item in enumerate(map_list):
        print(key + 1, ".", item)

    while True:
        try:
            a = int(input("Where do you want to go? "))
            print(a)
            if 0 < a <= len(map_list):
                return map_list[a - 1]
        except ValueError:
            print("Please enter a number! ")


def jump(player):
    for item in player.equipment:
        if item.name not in "parachute".lower():
            return False
    return True


def level_3():
    pass


def level_2(player):
    print("Good that you made it and didn't forget a parachute")
    player.respawn = 2
    player.level = 2
    for item in player.equipment:
        if item.name == "parachute":
            player.equipment.remove(item)
    print("You see a long road ahead! And few men in front take 'em one by one")
    print("Pick your weapon! (if you have any)")

    Enemies = [Enemy(1), Enemy(1), Enemy(2), Enemy(2), Enemy(3), Enemy(3)]
    for enemy in Enemies:
        if len(player.equipment) !=0:
            item_list = []
            for key, item in enumerate(player.equipment):
                print(item.name)
                item_list.append(str(key))
        else:
            print("You don't have any items! ")
            item_list = []
        while True:
            if len(player.equipment) != 0:
                ans = input("> ")
                if ans in item_list:
                    if len(player.equipment) != 0:
                        weapon_damage = player.equipment[int(ans)].damage
                    else:
                        weapon_damage = 0
                print("To fight press f[Enter] ASAP\n\n")
                while enemy.hp > 0:
                    fight = input("> ")
                    if fight == 'f':
                        enemy.get_hit(weapon_damage, player)
                    player.get_hit(3*enemy.level)
                    if player.hp <= 0:
                        player.hp = 100 * player.level
                        print("You died sorry for that, try again")
                        level_2(player)
                print("Congratulations you killed him move on to the nex t one or if it's the last one move on to lvl 3")

                break





def level_1(player):
    os.system("CLS")
    player.respawn = 1
    print("You're currently on a magic airplane and your task is to collect\n"
          "as much possible equipment as you can under 90 seconds.")
    print("To move you need to go to map view and than select where do you want to go")
    print("\n")
    print('"Map" --- see rooms your surrounded\n'
          '"Info" --- See your current stats\n'
          '"Save" --- to save your current status (feature to be added)')
    map_list = {
                "Ramp": ["Main Cabin"],
                "Main Cabin": ["Toilet", "Cockpit", "Ramp"],
                "Toilet": ["Main Cabin"],
                "Cockpit": ["Sleeping room", "Main Cabin"],
                "Sleeping room": ["Main Cabin"]
                }
    player.current_position = "Ramp"
    time = t()
    if True:
        items_ramp = [Equipment("Hammer"), Equipment("Gun"), Equipment("Bat")]
        items_cabin = [Equipment("Passport"), Equipment("Photos"), Equipment("Nail")]
        items_cockpit = [Equipment("Knife"), Equipment("Multi tool")]
        items_toilet = [Equipment("Paper")]
        items_sleep = [Equipment("parachute"), Equipment("Phone")]
        items_cabin[0].damage = 0
        items_cabin[1].damage = 0
        items_cabin[0].durability = 1
        items_cabin[1].durability = 1
        items_sleep[0].damage = 0
        items_sleep[1].damage = 0
        items_sleep[0].durability = 0
        items_sleep[1].durability = 0
    while t() - time < 30:
        answ = input("Your decision: ")
        if answ.lower() in ["map", "info", "save"]:
            if answ.lower() == "map":
                player.current_position = show_map(map_list[player.current_position])
            elif answ.lower() == "info":
                player.show_info()
            elif answ.lower() is "save":
                print("Feature to be added check git to be on latest version")
        else:
            print("Provide correct value! \n")

        if player.current_position == "Ramp":
            os.system("CLS")

            print("On your left is a chest. There might be something. Check it out")
            print("Type 'Chest' to open a chest")
            while True:
                a = input("> ")
                if a.lower() == "chest":
                    if not items_ramp:
                        print("There is nothing here!")
                        break
                    for item in items_ramp:
                        print("Name:       ", item.name)
                        print("Damage:     ", item.damage)
                        print("Durability: ", item.durability)
                    break
            print("\n If you want any, type it's name, if not type 'no'.")
            while True:
                dec = input("> ")
                if dec.lower() == "no":
                    break
                elif len(items_ramp) == 0:
                    break
                else:
                    item_name = []
                    for item in items_ramp:
                        item_name.append(item.name.lower())
                    if dec.lower() in item_name:
                        for item in items_ramp:
                            if dec in item.name.lower():
                                player.equipment.append(item)
                                print("You added", item.name, " to your equipment")
                                items_ramp.remove(item)

        elif player.current_position == "Main Cabin":
            os.system("CLS")

            print("You can check lockers above you to see if you can find anything interesting!")
            print("Type 'Locker' to open a locker")
            tru = False
            while True:
                a = input("> ")
                if a.lower() == "locker":
                    if not items_cabin:
                        print("There is nothing here!")
                        tru = True
                        break
                    for item in items_cabin:
                        print("Name:       ", item.name)
                        print("Damage:     ", item.damage)
                        print("Durability: ", item.durability)
                    break
            print("\n If you want any, type it's name, if not type 'no'.")
            while True and not tru:
                dec = input("> ")
                if dec.lower() == "no":
                    break
                elif len(items_cabin) == 0:
                    break
                else:
                    item_name = []
                    for item in items_cabin:
                        item_name.append(item.name.lower())
                    if dec.lower() in item_name:
                        for item in items_cabin:
                            if dec.lower() in item.name.lower():
                                player.equipment.append(item)
                                print("You added", item.name, " to your equipment")
                                items_cabin.remove(item)

        elif player.current_position == "Cockpit":
            os.system("CLS")
            print("You are now in a Cockpit. You can search pilots cubbys if you want.")
            print("Type 'Cubby' to open a cubby")
            while True:
                a = input("> ")
                if a.lower() == "cubby":
                    if not items_cockpit:
                        print("There is nothing here!")
                        break
                    for item in items_cockpit:
                        print("Name:       ", item.name)
                        print("Damage:     ", item.damage)
                        print("Durability: ", item.durability)
                    break
            print("\n If you want any, type it's name, if not type 'no'.")
            while True:
                dec = input("> ")
                if dec.lower() == "no":
                    break
                elif len(items_cockpit) == 0:
                    break
                else:
                    item_name = []
                    for item in items_cockpit:
                        item_name.append(item.name.lower())
                    if dec.lower() in item_name:
                        for item in items_cockpit:
                            if dec in item.name.lower():
                                player.equipment.append(item)
                                print("You added", item.name, " to your equipment")
                                items_cockpit.remove(item)

        elif player.current_position == "Toilet":
            os.system("CLS")
            print("Yo entered toilet. There is only one thing to take")
            print("Type 'Item' to see an item")
            while True:
                a = input("> ")
                if a.lower() == "item":
                    if not items_toilet:
                        print("There is nothing here!")
                        break
                    for item in items_toilet:
                        print("Name:       ", item.name)
                        print("Damage:     ", item.damage)
                        print("Durability: ", item.durability)
                    break
            print("\n If you want item type it's name, if not type 'no'.")
            while True:
                dec = input("> ")
                if dec.lower() == "no":
                    break
                elif len(items_toilet) == 0:
                    break
                else:
                    item_name = []
                    for item in items_toilet:
                        item_name.append(item.name.lower())
                    if dec.lower() in item_name:
                        for item in items_toilet:
                            if dec in item.name.lower():
                                player.equipment.append(item)
                                print("You added", item.name, " to your equipment")
                                items_toilet.remove(item)

        elif player.current_position == "Sleeping room":
            os.system("CLS")
            print("Sleeping room: Check under pillow to see if you can find anything")
            print("Type 'Pillow' to put it up")
            while True:
                a = input("> ")
                if a.lower() == "pillow":
                    if not items_sleep:
                        print("There is nothing here!")
                        break
                    for item in items_sleep:
                        print("Name:       ", item.name)
                    break
            print("\n If you want any, type it's name, if not type 'no'.")
            while True:
                dec = input("> ")
                if dec.lower() == "no":
                    break
                elif len(items_sleep) == 0:
                    break
                else:
                    item_name = []
                    for item in items_sleep:
                        item_name.append(item.name.lower())
                    if dec.lower() in item_name:
                        for item in items_sleep:
                            if dec in item.name.lower():
                                player.equipment.append(item)
                                print("You added", item.name, " to your equipment")
                                items_sleep.remove(item)

        elif len(player.equipment) == 11:
            break

    player.current_position = "Ramp"
    os.system("CLS")
    print("Time is up. Plane goes down. Now or never you have to jump")
    print("Hope you have everything!")
    print("")
    print("You see a man running in your direction with a knife in his hand.")
    print("What you do? ")
    print("1. Take some weapon out of your equipment")
    print("2. Jump out of the airplane now!")
    while True:
        ans = input("> ")
        ans_list = ['1', '2']
        if ans in ans_list:
            if ans == ans_list[0]:
                item_list = []
                for key, item in enumerate(player.equipment):
                    print(item.name)
                    item_list.append(str(key).lower())
                while True:
                    ans = input("> ")
                    if ans.lower() in item_list:
                        print("Good choice!")
                        print("man run next to you and umped out of the falling airplane.")
                        break
            if ans == ans_list[1]:
                for item in player.equipment:
                    print(item.name)
                if jump(player) == True:
                    level_2(player)
                else:
                    print("You don't have a parachute. You died where you 'landed'.")
                    s(2)
                    player.equipment = []
                    level_1(player)


def main():
    player = Hero()
    level_1(player)


if __name__ == "__main__":
    main()
