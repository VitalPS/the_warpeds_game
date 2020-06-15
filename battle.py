from time import sleep
from classes import Hero, Enemy
import effects
from random import randint


# criando heroi
hero_test = Hero('Tobs', 'Male', 100, 1, 'Psyco')
hero_test.battle_skills(50, 8, 6, 10)

# criando inimigo
drunk_man = Enemy('Drunk Man', 50, 7, 5, 9)


def fight(hero, enemy):
    round_counter = 0
    while hero.health > 0 and enemy.health > 0:
        round_counter += 1
        print(f'{effects.bold}{effects.red}{round_counter}º TURNO!{effects.normal}')    # contador de turnos

        current_enemy_attack = enemy.attacks[randint(0, len(enemy.attacks) - 1)]  # enemy attacks
        hero.health -= current_enemy_attack[0]
        print(f'{enemy.name} attacks you with a {current_enemy_attack[1]}.')

        current_hero_attack = hero.attacks[randint(0, len(hero.attacks) - 1)]  # hero attacks
        enemy.health -= current_hero_attack[0]
        print(f'{hero.name} attacks you with a {current_hero_attack[1]}.')

        print(f'Vida {hero} = {hero.health}')
        print(f'Vida {enemy} = {enemy.health}')
        sleep(0.5)
        print('-' * 30)

    if hero.health < 0:
        print(f'{hero} perdeu!')
    elif enemy.health < 0:
        print(f'{enemy} perdeu!')


# iniciando luta
fight(hero_test, drunk_man)
print(f'Sua vida final é igual a: {hero_test.health}')
