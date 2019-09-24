from random import randint


class Ability:
    def __init__(self, name, attack_strength):
        '''
            Create Instance Variables:
                name [string]
                max_damage [integer]
        '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        '''
            Returns a value between 0 and value set by self.max_damage
        '''
        attack_stat = randint(0, self.max_damage)
        return attack_stat


class Armor:
    def __init__(self, name, max_block):
        '''
            Instantiate instance properties.
                name [string]
                max_block [integer]
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
            Return a random value between 0 and the initialized self.max_block strength
        '''
        return randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health = 100):
        ''' 
          Instance properties:
          abilities [list]
          armors [list]
          name [string]
          starting_health [integer]
          current_health [integer]
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = []
        self.armors = []
        
    
    def add_ability(self, ability):
        '''
            function adds new abilities to abilities array
        '''
        self.abilities.append(ability)

    def attack(self):
        '''
            Calculates the total attack of all abilities and returns sum        
        '''
        attack_sum = 0
        for ability in self.abilities:
            attack_sum += ability.attack()
        return attack_sum

    def add_armor(self, armor):
        '''
            Adds armor to self.armor
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''
            Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total = 0
        for armor in self.armors:
            block_amount = armor.block()
            total += block_amount
        return abs(total - damage_amt)

    def take_damage(self, damage):
        '''
            Updates self.current_health to reflect the damage minus the defense.
        '''
        taken_damage = self.defend(damage)
        self.current_health = self.current_health - taken_damage

    def is_alive(self):  
        '''
            Return True or False depending on whether the hero fainted or not.
        '''
        return self.current_health > 0

    def fight(self, opponent):  
        ''' 
            Current Hero will take turns fighting the opponent hero passed in.
        '''
        # while both fighters are alive
        while True:
            if self.is_alive(): # check to see if user is still alive
                atk_pwr = self.attack() # will give character an attack value
                opponent.take_damage(atk_pwr) # opponent takes damage from self attacking opponent
            else: # opponent was too strong and you fainted
                print(f'Oh no! {opponent.name} was too strong. You lost all your health and fainted.')
                break
            if opponent.is_alive(): # check to see if opponent is alive
                atk_pwr = opponent.attack() # will give opponent an attack value
                self.take_damage(atk_pwr) # self will take damage from opponents attack
            else: # user was too strong and opponent fainted
                print(f'{self.name} beat {opponent.name}! Good job!')
                break

class Weapon(Ability):
    def attack(self):
        """  
            This method returns a random value
            between one half to the full attack power of the weapon.
        """
        half_atk = self.max_damage // 2
        return randint(half_atk,self.max_damage)

class Team:
    def __init__(self, name):
        ''' 
            Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        """
            Remove hero from hero list. If Hero isn't found return 0
        """
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''
            Prints out all heroes to the console.
        '''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''
        Add Hero object to self.heroes.
        '''
        self.heroes.append(hero)

if __name__ == '__main__':
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    