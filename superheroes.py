from random import randint, choice


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
        self.deaths = 0
        self.kills = 0

        # self.team = team_obj
        
    
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

    def view_stats(self):
        if self.deaths > 0:
            kd_ratio = self.kills // self.deaths
            return kd_ratio
        else:
            return self.kills
    def defend(self, damage_amt = 0 ):
        '''
            Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total = 0
        for armor in self.armors:
            total += armor.block
        return total

    def take_damage(self, damage):
        '''
            Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health -= damage - self.defend()

    def is_alive(self):  
        '''
            Return True or False depending on whether the hero fainted or not.
        '''
        return self.current_health > 0

    def add_kill(self, num_kills):
        ''' 
            Update self.kills with num_kills 
        '''
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        ''' 
            Update self.deaths with num_deaths
        '''
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''
            Add weapon to self.abilities
        '''
        self.abilities.append(weapon)
    
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
                opponent.add_kill(1)
                self.add_deaths(1)
                break
            if opponent.is_alive(): # check to see if opponent is alive
                atk_pwr = opponent.attack() # will give opponent an attack value
                self.take_damage(atk_pwr) # self will take damage from opponents attack
            else: # user was too strong and opponent fainted
                opponent.add_deaths(1)
                self.add_kill(1)
                break

class Arena:
    def __init__(self):
        '''
            Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team('Team A')
        self.team_two = Team('Team B')
    
    def create_ability(self):
        '''
            Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input('What abilities would you like your hero to have?')
        str_atk = input('How much attack power would you like your abilities to have?')
        attack_strength = int(str_atk)
        return Ability(name,attack_strength)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input('You get to choose a weapon, please name it: ')
        max_damage = int(input('how much can your weapon damage people? '))
        return Weapon(name, max_damage)
    
    def create_armor(self):
        '''
            Prompt user for Armor information
            return Armor with values from user input.
        '''
        name = input('Now you can choose some armour. Please type it in: ')
        max_block = int(input('Now how much defense would you like to add to your armour? '))
        return Armor(name, max_block)

    def create_hero(self):
        '''
            Prompt user for Hero information
            return Hero with values from user input.
        '''
        name = input('Please name your hero:')
        health = int(input('Please give your hero health! Otherwise he\'ll be at noob level:'))
        return Hero(name, health)

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        team_name = input('Welcome user! Please name the first team!')
        add_hero_to_one = input('Hello there, how many heroes would you like to add to team one?')
        self.team_one = Team(team_name)
        for _ in range(int(add_hero_to_one)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.
        team_name = input('Welcome user! Please name the second team!')
        add_hero_to_two = input('Hello there, how many heroes would you like to add to team two?')
        self.team_two = Team(team_name)
        for _ in range(int(add_hero_to_two)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        print(f'Working')
        self.team_one.attack(self.team_two)

    def show_stats(self):
       '''Prints team statistics to terminal.'''
       # TODO: This method should print out battle statistics
       # including each team's average kill/death ratio.
       # Required Stats:
       # Declare winning team
       # Show both teams average kill/death ratio.
       # Show surviving heroes.
       team_one_stats = self.team_one.stats()
       team_two_stats = self.team_two.stats()
       if team_one_stats > team_two_stats:
           print(f'{self.team_one.name} wins match!')
           print(f'These heroes are still alive on the team: ')
           for hero in self.team_one.heroes:
               print(f' - {hero.name}')
       elif team_one_stats < team_two_stats:
            print(f'{self.team_two.name} wins the match!')
            print(f'These heroes are still alive on this team: ')
            for hero in self.team_two.heroes:
                print(f' - {hero.name}')
       else:
            print(f'Match was a draw, no one wins.')

       print(f'Team {self.team_one.name} has an average ratio of {team_two_stats}.')
       print(f'Team {self.team_two.name} has an average ratio of {team_two_stats}.')


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

    def remainder_heroes(self):
        dead_hero = []
        alive_hero = []
        for hero in self.heroes:
            if hero.is_alive() == False:
                dead_hero.append(hero)
            else:
                alive_hero.append(hero)
        return dead_hero, alive_hero

    def attack(self, other_team):
        '''
            Battle each team against each other.
        '''
        print("Working attack")
        while len(self.remainder_heroes()[0]) < len(self.heroes) and len(other_team.remainder_heroes()[0]) < len(self.heroes):
            my_hero = choice(self.remainder_heroes()[1])
            opponent_hero  = choice(other_team.remainder_heroes()[1])
            my_hero.fight(opponent_hero)

    def revive_heroes(self, health=100):
        ''' 
            Reset all heroes health to starting_health
        '''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''
            Print team statistics
        '''
        sum = 0
        for hero in self.heroes:
            sum += hero.view_stats
            return  sum


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        print('Working')
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()