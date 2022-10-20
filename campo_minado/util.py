from fila import *


class PreencheComZero:
    def __init__(self) -> None:
        self._fila = Fila()

        self._fila.enqueue(0)

    def valoresVazio(self, linha, coluna, campo, campoJogador, tamanhoCampo):
        if (linha >= 0 and linha <= 3) and (coluna >= 0 and coluna <= 4):
            if campo[coluna][linha+1] == 0:
                self._fila.enqueue(campo[coluna][linha+1])
                campoJogador[coluna][linha+1] = 0
        if (linha >= 1 and linha <= 4) and (coluna >= 0 and coluna <= 4):
            if campo[coluna][linha-1] == 0:
                self._fila.enqueue(campo[coluna][linha-1])
                campoJogador[coluna][linha-1] = 0
        # verifica diagonal esquerda inferior
        if (linha >= 1 and linha <= tamanhoCampo-1) and (coluna >= 1 and coluna <= tamanhoCampo-1):
            if campo[coluna-1][linha-1] == 0:
                self._fila.enqueue(campo[coluna-1][linha-1])
                campoJogador[coluna-1][linha-1] = 0
        # verifica diagonal direita inferior
        if (linha >= 0 and linha <= tamanhoCampo-2) and (coluna >= 1 and coluna <= tamanhoCampo-1):
            if campo[coluna-1][linha+1] == 0:
                self._fila.enqueue(campo[coluna-1][linha+1])
                campoJogador[coluna-1][linha+1] = 0
        # verifica vertical inferior
        if (linha >= 0 and linha <= tamanhoCampo-1) and (coluna >= 1 and coluna <= tamanhoCampo-1):
            if campo[coluna-1][linha] == 0:
                self._fila.enqueue(campo[coluna-1][linha])
                campoJogador[coluna-1][linha] = 0
        # verifica diagonal direita superior
        if (linha >= 0 and linha <= tamanhoCampo-2) and (coluna >= 0 and coluna <= tamanhoCampo-2):
            if campo[coluna+1][linha+1] == 0:
                self._fila.enqueue(campo[coluna+1][linha+1])
                campoJogador[coluna+1][linha+1] = 0
        # verifica diagonal esquerda superior
        if (linha >= 1 and linha <= tamanhoCampo-1) and (coluna >= 0 and coluna <= tamanhoCampo-2):
            if campo[coluna+1][linha-1] == 0:
                self._fila.enqueue(campo[coluna+1][linha-1])
                campoJogador[coluna+1][linha-1] = 0
        # verifica vertical superior
        if (linha >= 0 and linha <= tamanhoCampo-1) and (coluna >= 0 and coluna <= tamanhoCampo-2):
            if campo[coluna+1][linha] == 0:
                self._fila.enqueue(campo[coluna+1][linha])
                campoJogador[coluna+1][linha] = 0
        self._fila.dequeue()

        return campoJogador
