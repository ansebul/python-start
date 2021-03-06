
import re

class Goose:

    def __init__(self, name, eggs=0, weight=5, voice='Krya!'):
        self.name = name
        self.eggs = eggs
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.eggs += 1

    def get_eggs(self):
        if self.eggs > 0:
            self.weight -= 1
            self.eggs -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


class Cow:

    def __init__(self, name, milk=0, weight=200, voice='Muuu!'):
        self.name = name
        self.milk = milk
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.milk += 1

    def get_milk(self):
        if self.milk > 0:
            self.weight -= 1
            self.milk -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


class Chicken:

    def __init__(self, name, eggs=0, weight=4, voice='Ko-ko-ko!'):
        self.name = name
        self.eggs = eggs
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.eggs += 1

    def get_eggs(self):
        if self.eggs > 0:
            self.weight -= 1
            self.eggs -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


class Sheep:

    def __init__(self, name, wool=0, weight=20, voice='Beee!'):
        self.name = name
        self.wool = wool
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.wool += 1

    def get_wool(self):
        if self.wool > 0:
            self.weight -= 1
            self.wool -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


class Goat:

    def __init__(self, name, milk=0, weight=15, voice='Meee!'):
        self.name = name
        self.milk = milk
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.milk += 1

    def get_milk(self):
        if self.milk > 0:
            self.weight -= 1
            self.milk -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


class Duck:

    def __init__(self, name, eggs=0, weight=8, voice='Krya-krya!'):
        self.name = name
        self.eggs = eggs
        self.weight = weight
        self.voice = voice

    def eat(self, food):
        self.weight += food
        self.eggs += 1

    def get_eggs(self):
        if self.eggs > 0:
            self.weight -= 1
            self.eggs -= 1
        else:
            self.say()

    def say(self):
        print(self.voice)


animals = []

animals.append(Goose('??????????'))
animals.append(Goose('??????????'))
animals.append(Cow('????????????'))
animals.append(Sheep('??????????????'))
animals.append(Sheep('????????????????'))
animals.append(Chicken('????-????'))
animals.append(Chicken('????????????????'))
animals.append(Goat('????????'))
animals.append(Goat('????????????'))
animals.append(Duck('????????????'))

# Feed & milk (if need)
for animal in animals:
    food = animal.weight / 4
    animal.eat(food)
    if hasattr(animal, 'eggs'):
        animal.get_eggs()
    if hasattr(animal, 'milk'):
        animal.get_milk()
    if hasattr(animal, 'wool'):
        animal.get_wool()

# Collect final statistics
weight_by_animal_type = {}
recordsman = ''
max_weight = 0

for animal in animals:
    animal_type = re.findall(r'^<class\ \'__main__\.(\w+)\'>$', str(type(animal)))
    if animal_type[0] in weight_by_animal_type:
        weight = weight_by_animal_type.get(animal_type[0]) + animal.weight
        weight_by_animal_type.update({animal_type[0]: weight})
    else:
        weight_by_animal_type.update({animal_type[0]: animal.weight})

    if animal.weight > max_weight:
        max_weight = animal.weight
        recordsman = animal.name

for animal_class, total_weight in weight_by_animal_type.items():
    print(f'?????? ???????????????????? ???????????? {animal_class} ?????????? {total_weight} ????')

print(f'?????????? ?????????????? ???????????????? ?????????? {recordsman}, ?????? ?????? {max_weight}')

