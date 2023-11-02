from random import choice
lista=['PEDRA','PAPEL','TESOURA']
pc=choice(lista)

print('='*40)
print('      Jogo de Pedra Papel Tesoura')
print('='*40)
while True:
    jogador=input(str('Escolha entre Pedra, Papel ou Tesoura: ')).upper()
    print(jogador)
    print('-'*40)
    print(f'Voce jogou {jogador} e o computador jogou {pc}')
    print('-'*40)

    if jogador==pc:
        print('Deu empate, tente novamente!')
    elif jogador=='PEDRA' and pc=='TESOURA':
        print('Parabéns, você ganhou!!!')
        break
    elif jogador=='PAPEL' and pc=='PEDRA':
        print('Parabéns, você ganhou!!!')
        break
    elif jogador=='TESOURA' and pc=='PAPEL':
        print('Parabéns, você ganhou!!!')
        break
    else:
        print('Voce perdeu, tente novamente!')
    print('='*40)