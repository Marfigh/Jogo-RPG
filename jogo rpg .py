print('           #ECHOES OF DARKNESS#\n')
print('Olá jogaddor seja muito bem vindo ao mundo de Darkness')
nome=input('Qual seu nome aventureiro(a)?\n')
print('Seja muito bem vindo(a) {}\n'. format(nome))
print('O jogo funciona da seguinte forma')
print('No menu de ações você vai ter 3 opções:\n')
print('Atacar: Tira 20 de vida do monstro mais você acaba perdendo 15 de vida')
print('Poção: Reculpera 25 de vida do herói mais gasta 1 poção')
print('Status: Mostra a vida do monstro, vida do herói e quatas poções o jogador tem\n')
print('Boa sorte jogador para enfrentar a terrível fera, seja esperto e ........\n')
pocao=2
vheroi=100
vvilao=120
while True:
    print('         **-Menu de Ações-**\n')
    print('1 - Atacar')
    print('2 - Usar poção')
    print('3 - Ver status\n')
    acao=int(input('Digite o que você deseja fazer\n'))
    while acao != 1 and acao != 2 and acao != 3:
        print('Digite uma opção valida {}'. format(nome))
        acao=int(input('Digite o que você deseja fazer'))
    if acao == 1:
        print('Você atacou o vilão mais se feriu um pouco\n')
        vheroi=vheroi - 15
        vvilao=vvilao - 20
        if vheroi <= 0:
            print('Game Ouver mané')
        if vvilao <= 0:
            print('PARABÉNSSS HERÓI')
            print('Você matou o monstro')
    if acao == 2:
        if pocao == 0:
            print('Suas poções acabaram!!!\n')
        if pocao >= 1:
            print('Você acaba de usar a poção, se sente bem mais FORTE agora')
            vheroi<=150
            vheroi=vheroi + 25
            pocao=pocao - 1
            if vheroi > 150:
                vheroi = 150
    if acao == 3:
        print('Vida do Herói: {} HP'. format(vheroi))
        print('Vida do Vilão: {} HP'. format(vvilao))
        print('Quantidade de Poções é: {} poções\n'.format(pocao))
    if vvilao > 0 and vheroi > 0:
        voltar=int(input('Se deseja voltar ao menu digite 5\n'))
        if voltar == 5:
            print('Voltando .....')
    else:
        break






