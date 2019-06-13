import json
import random


class Hero:
    def __init__(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.email = input("Email: ")
        self.spells = []
        self.level = 1
        self.hp = 100 * self.level
        self.equipment = []
        self.respawn = None
        self.current_position = None

    def print_name(self):
        print(self.name)

    # def save_data(self):
    #     with open("data.json", "r") as file:
    #         old_data = json.load(file)
    #         print(old_data)
    #         # data = {"name": self.name, "age": self.age, "email": self.email}
    #         # json.dump(data, file)

    def get_hit(self, hp):
        self.hp -= hp

    def add_equipment(self, equip):
        self.equipment.append(equip)

    def show_info(self):
        print("User name: ", self.name)
        print("User hp: ", self.hp)
        if len(self.equipment) != 0:
            print("Equipment: ")
            for key, value in enumerate(self.equipment):
                print(key, ".", value.name)
        print("User level: ", self.level)


class Equipment:
    def __init__(self, name):
        self.name = name
        self.damage = random.randint(10, 70)
        self.durability = random.randint(20, 30)

    def hit(self):
        self.durability -= 1


class Enemy:
    def __init__(self, lvl):
        self.names = ['James', 'Jon', 'John', 'Robert', 'Michael', 'Mary', 'Patricia', 'Linda']
        self.name = random.choice(self.names)
        self.level = lvl
        self.hp = random.randint(100, 200) * self.level
        self.spells = []
        self.equipment = []

    def add_equipment(self, equip):
        self.equipment.append(equip)

    def get_hit(self, dmg, player):
        self.hp -= dmg * player.level










