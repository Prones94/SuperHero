class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')

# class Dog(Animal):
#     def bark(self):
#         print('Woof! Woof!')

cat = Animal('DJ')
cat.eat()
cat.drink()