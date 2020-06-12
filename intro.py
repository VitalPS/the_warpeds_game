from time import sleep
from classes import Hero


print('Bem vindo ao The Warpeds...')
sleep(2)

print('-' * 30)
# 1 - Definindo o nome
name = str(input('Por favor, digite o seu nome: '))
sleep(2)
print(f'Que belo nome, {name}!')
sleep(2)

print('-' * 30)
# 2 - Definindo o gênero
print('Sinto muito! Meus processadores foram bastante corroídos em decorrência do GRANDE DIA.')
sleep(3)
gender = str(input('''Não consigo identificar o seu gênero. Poderia definí-lo para mim, por favor? 
[1] Masculino
[2] Feminino
[3] Não definido
Qual a sua opção? '''))
sleep(2)

while gender not in '123':
    gender = str(input('''Ops! Acho que esta opção não está no meu banco de dados. 
    Poderia repetir, por favor?
    Lembrando: [1] Masculino, [2] Feminino e [3] Não definido.
    Digite a sua opção: '''))
sleep(2)

if gender in '1':
    gender_id = 'Masculino'
    print('Perfeito! Seu genero foi registrado como Masculino!')
elif gender in '2':
    gender_id = 'Feminino'
    print('Perfeito! Seu genero foi registrado como Feminino!')
else:
    gender_id = 'Indefinido'
    print('Bom, gênero é mesmo uma coisa muito complicada, não é mesmo!?')
sleep(2)


print('-' * 30)
# 3 - Definindo a idade
print('Me pergunto se você conseguirá realmente vencer The Warpeds...')
sleep(1)
print('Digo de antemão que esta não é uma jornada muito fácil!')
sleep(1)
age = int(input('Por favor, digite a sua idade (anos): '))
sleep(2)

while age <= 5 or age >= 60:
    if age <= 5:
        x = str(input('''Acho que você está muito jovem para uma aventura neste porte.
              Tem certeza que deseja continuar!? [Y]/[N] '''))
        while x not in 'yn':
            x = input('Opção inválida! Por favor escolha se você quer[Y] ou não[N] continuar com esta idade: ')
        else:
            if x in 'Y':
                print('Bom, não diga que eu não avisei...')
                sleep(2)
            else:
                age = int(input('Ok então. Por favor re-digite a sua idade (anos): '))
                sleep(2)

    elif age >= 60:
        x = str(input('''Acho que você está muito acima da idade para uma aventura neste porte.
        Tem certeza que deseja continuar!? [Y]/[N] '''))
        while x not in 'yn':
            x = input('Opção inválida! Por favor escolha se você quer[Y] ou não[N] continuar com esta idade: ')
        else:
            if x in 'y':
                print('Bom, não diga que eu não avisei...')
                sleep(2)
            else:
                age = int(input('Ok então. Por favor re-digite a sua idade (anos): '))
                sleep(2)

else:
    print(f'Anotado! Sua idade é {age} anos!')
    print('Acho que podemos, enfim, definir suas características.')
sleep(2)


print('-' * 30)
# 4 - Definindo a classe do heroi
feat = str(input('''Se fosse para você escolher duas vantagens e um defeito? Quais seriam?
[1] Forte e resistente, mas nada esperto
[2] Estratégico e acrobático, mas muito frágil
[3] Inteligente e criativo, mas antissocial
Digite a sua opção: '''))

while feat not in '123':
    feat = str(input('''Ops! Acho que houve um mal entendido aqui. 
    Poderia a sua escolha novamente, por favor?
    Lembrando:
    [1] Forte e resistente, mas pouco inteligente
    [2] Perceptível e ágil, mas pouco resistente
    [3] Inteligente e sortudo, mas pouco carismático
    Digite a sua opção: '''))
sleep(2)


if feat in '1':
    feat_id = 'Psicótico'
    print('Bem que eu achei que você tinha uma cara de doido! Sua classe é Psicótico!')
elif feat in '2':
    feat_id = 'Assassino'
    print('É bom que eu seja seu amigo. Detesto ter um Assasino como inimigo!')
else:
    feat_id = 'Neurótico'
    print('Não consegue controlar as suas ideias na sua cabeça, não é!? Típico de um Neurótico.')
sleep(2)


print('-' * 30)
# Criando heroi
hero = Hero(name, gender_id, age, feat_id)
hero.attributes()

if feat in '1':
    hero.strength += 2
    hero.endurance += 2
    hero.intelligence -= 3
elif feat in '2':
    hero.perception += 2
    hero.agility += 2
    hero.endurance -= 3
else:
    hero.intelligence += 2
    hero.luck += 2
    hero.charisma -= 3

print(f'''RESUMO DA ÓPERA:
- Nome: {hero.name}
- Gênero: {hero.gender_id}
- Idade: {hero.age}
- Classe: {hero.feat_id}

ATRIBUTOS:
Força: {hero.strength}
Percepção: {hero.perception}
Resistência: {hero.endurance}
Carisma: {hero.charisma}
Inteligência: {hero.intelligence}
Agilidade: {hero.agility}
Sorte: {hero.luck}''')
