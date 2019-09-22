# my-dogs.py
import dog # we need to specify exactly what we want

my_dog = dog.Dog('Rex', 'SuperDog')
my_other_dog = dog.Dog('Annie', 'SuperDog')
my_mini_dog = dog.Dog('Mister Butterscotch', 'WienerDog')
my_wolf_dog = dog.Dog('White Fang', 'DireWolf')
my_corgi_dog = dog.Dog('Cupcake', 'Corgi')

print(f'{my_other_dog.name}, the {my_other_dog.breed}')
my_other_dog.bark()
my_other_dog.roll()
my_other_dog.sit()
print(f'{my_mini_dog.name}, the {my_mini_dog.breed}')
my_mini_dog.bark()
print(f'{my_corgi_dog.name}, the {my_corgi_dog.breed}')
my_corgi_dog.bark()
print(f'{my_wolf_dog.name}, the {my_wolf_dog.breed}')
my_dog.bark()

my_other_dog.bark()
my_wolf_dog.bark()
my_corgi_dog.bark()
