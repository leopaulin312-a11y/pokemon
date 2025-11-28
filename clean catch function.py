from random import randint
import random

num_balls = 5  # Example number of Pokeballs; in practice, this would be dynamic

class Pokemon:
    def __init__(self, name, max_hp, catch_rate):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.catch_rate = catch_rate
        self.is_caught = False

pokemon_list = [
    Pokemon("Charizard", 156, 45),
    Pokemon("Gyarados", 170, 45),
    Pokemon("Lucario", 145, 45),
    Pokemon("Gardevoir", 150, 45),
    Pokemon("Tyranitar", 180, 45),
    Pokemon("Greninja", 140, 45),
    Pokemon("Garchomp", 180, 45),
    Pokemon("Blaziken", 155, 45),
    Pokemon("Metagross", 170, 3),
    Pokemon("Umbreon", 200, 45),
    Pokemon("Oshawott", 120, 45)
]

pokemon_random = random.choice(pokemon_list)

ball_ratio ={1: 1.0,   # Pokeball
                 2: 1.5,   # Greatball
                 3: 2.0}   # Ultraball

def catch_chance(pokemon, ball_ratio):
    hp_factor = (3 * pokemon.max_hp - 2 * pokemon.hp) / (3 * pokemon.max_hp)
    return hp_factor * pokemon.catch_rate * ball_ratio

def catch_attempt(catch_chance):
    if catch_chance >= 255:
        return True
    
    treshold = 65535 * (0.25 ** (catch_chance / 255))
    for i in range (4):
        if randint(0, 65535) > treshold:
            return False
    return True

def throw_pokeball(pokemon, ball_type):
    ratio = ball_ratio.get(ball_type, 1.0)
    catch_chance_value = catch_chance(pokemon, ratio)
    if catch_attempt(catch_chance_value):
        print(f'you caught {pokemon.name} !')
        pokemon.is_caught = True
        return True
    else:
        print(f'{pokemon.name} broke free from the pokeball !') 
    return False

print(f'a wild {pokemon_random.name} appeared !')

throw_ball = input('do you want to throw a pokeball ? (yes/no): ')

if throw_ball == 'yes':
    print('which ball do you want to use ?')
    print('1-- pokeball')
    print('2-- great ball')
    print('3-- ultra ball')
    ball_type = int(input('select the type of ball: '))
    throw_pokeball(pokemon_random, ball_type)  
    num_balls -= 1

    print(f'you have {num_balls} balls left.')
    while pokemon_random.is_caught == False and num_balls > 0:
        ball_type = int(input('select the type of ball: '))
        throw_pokeball(pokemon_random, ball_type)
        num_balls -= 1
        
        print(f'you have {num_balls} balls left.')
        
        if pokemon_random.is_caught:
            break

        if num_balls == 0:
            print('you have no balls left !')
            break
        
        rethrow=input('do you want to throw another ball ? (yes/no): ')
        if rethrow != 'yes':
           break

else:
    pass
