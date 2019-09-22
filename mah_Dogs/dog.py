# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def roll(self):
        print(f'{self.name} rolls')

    def sit(self):
        print(f'{self.name} sits')

Dog.greeting = 'Whoa!'