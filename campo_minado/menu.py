from jogo import *
from campo import *


def menu():
    print("=*= Campo Minado =*=")
    tamanhoCampo = int(
        input("Digite o tamanho do campo (Deve ser maior ou igual a 5): "))
    bombas = int(input("Quantidade de bombas: "))

    if bombas > tamanhoCampo:
        return print('\nNumero de bombas nao pode ser maior que o campo!')
    jogo = Campo(tamanhoCampo, bombas)
    campo = jogo.criaCampo()
    jogador = jogo.criaCampoJogador()
    operacao = Jogo(tamanhoCampo)
    while True:
        if operacao.checarVitoria(jogador) == False:
            jogo.mostraCampoJogador()
            pontoX = int(input("linha(1 a {}): ".format(tamanhoCampo)))
            pontoY = int(input("coluna:(1 a {}) ".format(bombas)))
            operacao.verificaJogada(pontoX - 1, pontoY - 1, campo, jogador)
            if campo[pontoY - 1][pontoX - 1] == 'X':
                jogo.mostraCampo()
                break
        else:
            jogo.mostraCampoJogador()
            print('Parabéns, você venceu!')


menu()
