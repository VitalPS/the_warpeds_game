from time import sleep
from classes import Hero
import effects
import dialog


print(f'{effects.red}{effects.framed}{effects.bold} Bem vindo ao The Warpeds... {effects.reset}{effects.yellow}')
sleep(2)

# 1 - Definindo o nome
name = str(input(dialog.name_choice['input']).capitalize().strip())
sleep(2)
print(dialog.name_choice['success'].format(name))
sleep(2)

print('-' * 30)
# 2 - Definindo o gênero
print(dialog.gender_choice['intro'])
print('-' * 30)
sleep(3)
gender = str(input(dialog.gender_choice['input']))
sleep(2)

while gender not in '123':
    print('-' * 30)
    gender = str(input(dialog.gender_choice['invalid_option']))
sleep(2)

if gender in '1':
    gender_id = 'Masculino'
    print('-' * 30)
    print(dialog.gender_choice['success_masculine'])
elif gender in '2':
    gender_id = 'Feminino'
    print('-' * 30)
    print(dialog.gender_choice['success_feminine'])
else:
    gender_id = 'Indefinido'
    print('-' * 30)
    print(dialog.gender_choice['success_undefined'])
sleep(2)


print('-' * 30)
# 3 - Definindo a idade
print(dialog.age_choice['intro_1'])
sleep(2)
print(dialog.age_choice['intro_2'])
sleep(2)
print('-' * 30)


age = int(input(dialog.age_choice['input']))
sleep(2)

while age <= 5 or age >= 60:        # todo colocar dentro de uma função
    if age <= 5:
        print('-' * 30)
        x = str(input(dialog.age_choice['too_young']))
        while x not in 'yn':
            print('-' * 30)
            x = input(dialog.age_choice['invalid_option'])
        else:
            if x in 'Y':
                print('-' * 30)
                print(dialog.age_choice['warning'])
                sleep(2)
            else:
                print('-' * 30)
                age = int(input(dialog.age_choice['re_input']))
                sleep(2)

    elif age >= 60:         # todo colocar dentro de uma função
        print('-' * 30)
        x = str(input(dialog.age_choice['too_old']))
        while x not in 'yn':
            print('-' * 30)
            x = input(dialog.age_choice['invalid_option'])
        else:
            if x in 'y':
                print('-' * 30)
                print(dialog.age_choice['warning'])
                sleep(2)
            else:
                print('-' * 30)
                age = int(input(dialog.age_choice['re_input']))
                sleep(2)

else:
    print('-' * 30)
    print(dialog.age_choice['success'].format(age))
sleep(2)


print('-' * 30)
# 4 - Definindo a classe do heroi
print(dialog.class_choice['intro'])
print('-' * 30)
sleep(2)
feat = str(input(dialog.class_choice['input']))
sleep(2)

while feat not in '123':
    print('-' * 30)
    feat = str(input(dialog.class_choice['invalid_option']))
sleep(2)


if feat in '1':
    feat_id = 'Psicótico'
    print('-' * 30)
    print(dialog.class_choice['success_class_1'])
elif feat in '2':
    feat_id = 'Assassino'
    print('-' * 30)
    print('success_class_2')
elif feat in '3':
    feat_id = 'Neurótico'
    print('-' * 30)
    print('success_class_3')
sleep(3)


print('-' * 30)
# Criando heroi
hero = Hero(name, gender_id, age, feat, feat_id)
hero.attributes()

if feat in '1':
    hero.strength += 2
    hero.endurance += 2
    hero.intelligence -= 3
elif feat in '2':
    hero.perception += 2
    hero.dextery += 2
    hero.endurance -= 3
elif feat in '3':
    hero.intelligence += 2
    hero.luck += 2
    hero.charisma -= 3


print('E aqui vai um resumo do seu personagem!!')
sleep(5)
print('-' * 30)
print(f'''{effects.bold}CARACTERÍSTICAS PRINCIPAIS:{effects.reset}
- Nome: {hero.name}
- Gênero: {hero.gender_id}
- Idade: {hero.age}
- Classe: {hero.feat_id}

{effects.bold}ATRIBUTOS:{effects.reset}
- Força: {hero.strength}
- Percepção: {hero.perception}
- Resistência: {hero.endurance}
- Carisma: {hero.charisma}
- Inteligência: {hero.intelligence}
- Agilidade: {hero.dextery}
- Sorte: {hero.luck}''')
