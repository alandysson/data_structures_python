from campo import *
from fila import *
from util import *


class Jogo:
    def __init__(self, tamanhoCampo) -> None:
        self._tamanhoCampo = tamanhoCampo
        self._imprimirZero = PreencheComZero()

    def verificaJogada(self, x, y, campo, campoJogador):
        if campo[y][x] == 0:
            campoJogador[y][x] = campo[y][x]
            campoJogador = self._imprimirZero.valoresVazio(
                x, y, campo, campoJogador, self._tamanhoCampo)
        elif campo[y][x] != 'X':
            campoJogador[y][x] = campo[y][x]
        elif campo[y][x] == 'X':
            print("Você perdeu!")

    def checarVitoria(self, campoJogador):
        for linha in campoJogador:
            for pixel in linha:
                if pixel == '-':
                    return False
        return True
