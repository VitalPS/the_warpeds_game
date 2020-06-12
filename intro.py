from pygame import time
from classes import Hero

print('Bem vindo ao The Warpeds...')
time.wait(2000)

print('-'* 30)
# 1 - Definindo o nome
name = str(input('Por favor, digite o seu nome: '))
time.wait(2000)
print(f'Que belo nome, {name}!')
time.wait(2000)


print('-'* 30)
# 2 - Definindo o gênero
print('Sinto muito! Meus processadores foram bastante corroídos em decorrência do GRANDE DIA.')
time.wait(3000)
gender = str(input('''Não consigo identificar o seu gênero. Poderia definí-lo para mim, por favor? 
[1] Masculino
[2] Feminino
[3] Não definido
Qual a sua opção? '''))
time.wait(2000)

while gender not in '123':
    gender = str(input('''Ops! Acho que esta opção não está no meu banco de dados. 
    Poderia repetir, por favor?
    Lembrando, [1] Masculino, [2] Feminino e [3] Não definido.
    Digite a sua opção: '''))
time.wait(2000)

if gender in '1':
    gender_id = 'Masculino'
    print('Perfeito! Seu genero foi registrado como Masculino!')
elif gender in '2':
    gender_id = 'Feminino'
    print('Perfeito! Seu genero foi registrado como Feminino!')
else:
    gender_id = 'Indefinido'
    print('Bom, gênero é mesmo uma coisa muito complicada, não é mesmo!?')
time.wait(2000)


print('-'* 30)
# 3 - Definindo a idade
print('MAS, será que você conseguirá realmente vencer The Warpeds?')
print('Digo de antemão que esta não é uma jornada muito fácil...')
age = int(input('Por favor, digite a sua idade (anos): '))
time.wait(1000)

while age <= 5 or age >= 60:
    if age <= 5:
        x = str(input('''Acho que você está muito jovem para uma aventura neste porte.
              Tem certeza que deseja continuar!? [Y]/[N] '''))
        while x not in 'yn':
            x = input('Opção inválida! Por favor escolha se você quer[Y] ou não[N] continuar com esta idade: ')
        else:
            if x in 'Y':
                print('Bom, não diga que eu não avisei...')
                time.wait(1000)
            else:
                age = int(input('Ok então. Por favor re-digite a sua idade (anos): '))
                time.wait(1000)

    elif age >= 60:
        x = str(input('''Acho que você está muito acima da idade para uma aventura neste porte.
                      Tem certeza que deseja continuar!? [Y]/[N] '''))
        while x not in 'yn':
            x = input('Opção inválida! Por favor escolha se você quer[Y] ou não[N] continuar com esta idade: ')
        else:
            if x in 'y':
                print('Bom, não diga que eu não avisei...')
                time.wait(1000)
            else:
                age = int(input('Ok então. Por favor re-digite a sua idade (anos): '))
                time.wait(1000)

else:
    print('Acho que podemos, enfim, definir suas características.')
time.wait(1000)


print('-'* 30)
# 4 - Definindo a classe do heroi
feat = str(input('''E se fosse para você escolher duas vantagens e um defeito? Quais seriam?
[1] Forte e resistente, mas nada esperto
[2] Estratégico e acrobático, mas muito frágil
[3] Inteligente e criativo, mas antissocial
'''))





# Criando heroi
hero = Hero(name, gender_id, age, feat)

print(f'''RESUMO DA ÓPERA:
- Nome: {hero.name}
- Gênero: {hero.gender_id}
- Idade: {hero.age}
- Classe: {hero.feat}''')
