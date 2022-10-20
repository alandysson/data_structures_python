from random import randint


class Campo:
    def __init__(self, tamanhoCampo, bombas):
        self._matriz = []
        self._matrizJogador = []
        self._tamanhoCampo = tamanhoCampo
        self._bombas = bombas

    def criaCampoJogador(self):
        self._matrizJogador = [['-' for linha in range(
            self._tamanhoCampo)] for coluna in range(self._tamanhoCampo)]

        return self._matrizJogador

    def criaCampo(self):
        self._matriz = [[0 for linha in range(
            self._tamanhoCampo)] for coluna in range(self._tamanhoCampo)]

        for x in range(self._bombas):
            bombaLinha = randint(0, self._tamanhoCampo - 1)
            bombaColuna = randint(0, self._tamanhoCampo - 1)
            self._matriz[bombaColuna][bombaLinha] = 'X'  # adiciona bomba
            self.adicionaValores(bombaLinha, bombaColuna)

        return self._matriz

    def adicionaValores(self, linha, coluna):
        # verifica linhas horizontais
        if (linha >= 0 and linha <= 3) and (coluna >= 0 and coluna <= 4):
            if self._matriz[coluna][linha+1] != 'X':
                self._matriz[coluna][linha+1] += 1
        if (linha >= 1 and linha <= 4) and (coluna >= 0 and coluna <= 4):
            if self._matriz[coluna][linha-1] != 'X':
                self._matriz[coluna][linha-1] += 1
        # verifica diagonal esquerda inferior
        if (linha >= 1 and linha <= self._tamanhoCampo-1) and (coluna >= 1 and coluna <= self._tamanhoCampo-1):
            if self._matriz[coluna-1][linha-1] != 'X':
                self._matriz[coluna-1][linha-1] += 1
        # verifica diagonal direita inferior
        if (linha >= 0 and linha <= self._tamanhoCampo-2) and (coluna >= 1 and coluna <= self._tamanhoCampo-1):
            if self._matriz[coluna-1][linha+1] != 'X':
                self._matriz[coluna-1][linha+1] += 1
        # verifica vertical inferior
        if (linha >= 0 and linha <= self._tamanhoCampo-1) and (coluna >= 1 and coluna <= self._tamanhoCampo-1):
            if self._matriz[coluna-1][linha] != 'X':
                self._matriz[coluna-1][linha] += 1
        # verifica diagonal direita superior
        if (linha >= 0 and linha <= self._tamanhoCampo-2) and (coluna >= 0 and coluna <= self._tamanhoCampo-2):
            if self._matriz[coluna+1][linha+1] != 'X':
                self._matriz[coluna+1][linha+1] += 1
        # verifica diagonal esquerda superior
        if (linha >= 1 and linha <= self._tamanhoCampo-1) and (coluna >= 0 and coluna <= self._tamanhoCampo-2):
            if self._matriz[coluna+1][linha-1] != 'X':
                self._matriz[coluna+1][linha-1] += 1
        # verifica vertical superior
        if (linha >= 0 and linha <= self._tamanhoCampo-1) and (coluna >= 0 and coluna <= self._tamanhoCampo-2):
            if self._matriz[coluna+1][linha] != 'X':
                self._matriz[coluna+1][linha] += 1

    def mostraCampo(self) -> str:
        for linha in self._matriz:
            print("\t".join(str(celula) for celula in linha))
            print("")

    def mostraCampoJogador(self):
        for linha in self._matrizJogador:
            print("\t".join(str(celula) for celula in linha))
            print("")


if __name__ == "__main__":
    x = Campo(5, 5)
    x.criaCampoJogador()
    x.mostraCampoJogador()
