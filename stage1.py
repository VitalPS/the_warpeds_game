import dialog
from time import sleep

conves = ('Inicio.', 'dialog.conves_choice')
escada = ('Ir para a escada.', 'Você sobe as escadas.')
conversa = ('Conversar com um bêbado.', 'Você conversa com o cara e toma um soco. PERDEU 5 DE VIDA!')
porta = ('Abrir porta.', 'A porta se abre. Você entra na sala do capitão.')
superficie_navio = ('Ir para a cobertura do navio', 'Você se encontra em um GRANDE NAVIO PIRATA!')
espada = ('Pegar espada?', 'Você pega a espada do capitão!')
armario = ('Se esconder no armário.', 'Você esconde no armário. Nada acontece.')
deposito = ('Entrar no depósito do navio.', 'Você entra no depósito e vê vários barris cheios e vazios.')
barril = ('Se esconder em um barril', 'Este parece ser um bom lugar para se esconder de um desastre. Nada acontece.')
proa = ('Ir para a proa do navio.', 'Você esta na proa do navio.')
capitao = ('Conversar com o capitão do navio.', 'Ele olha para você com uma cara de desconfiado.')
ver_mar = ('Olhar para o mar.', 'Você olha para o mar e vê que ele está repleto de tubarões!!')
pular_no_mar = ('Pular no mar.', 'Você é devorado por vários tubarões. PERDEU JOGO!')
fim_jogo = ( ),


bifurcacoes = {
    conves: (escada, porta, conversa, armario),
    escada: (superficie_navio, conves),
    conversa: (conves,),
    porta: (conves, espada, ),
    espada: (conves, ),
    armario: (conves,),
    superficie_navio: (escada, deposito, proa, capitao),
    capitao: (fim_jogo, ),
    deposito: (superficie_navio, barril, ),
    barril: (deposito, ),
    proa: (ver_mar, pular_no_mar,),
    ver_mar: (proa, ),

}

localizacao = conves  # onde você começa
print('''Você acorda em em uma sala de madeira suja e mofada todo molhado.
Várias pessoas estão ao seu redor. A situação delas parece ser a mesma que a sua!''')

while True:
    try:
        print(localizacao[1])

        for i, j in enumerate(bifurcacoes[localizacao]):
            print('[', i + 1, ']', j[0])
        print(' ')
        escolha = int(input('Qual a sua escolha? '))
        localizacao = bifurcacoes[localizacao][escolha - 1]
        print('-' * 30)
    except:
        print('MEUS PARABÉNS VOCE ACABA DE FINALIZAR WARPEDS')
        break