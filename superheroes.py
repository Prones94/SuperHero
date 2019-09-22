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

if __name__ == '__main__':
    ability = Ability('Debugging Ability', 20)
    print(ability.name)
    print(ability.attack())