import random


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
        attack_stat = random.randint(0, self.max_damage)
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
        block_stat = random.randint(0, self.max_block)
        return block_stat


class Hero:
    def __init__(self, name, abilities, starting_health = 100, current_health = 100):
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
        self.current_health = current_health
        self.abilities = []
        # self.armor = armor
        
    
    def add_abilities(self, ability):
        self.abilities.append(ability)

        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use
        # pass


if __name__ == '__main__':
    ability = Ability('Debugging Ability', 50)
    defense = Armor('Turtle Armor', 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_abilities(ability)
    print(hero.abilities)
    print(ability.name)
    # print(defense.name)
    print(ability.attack())
    # print(defense.block())
