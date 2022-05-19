from random import randrange


class Campo:
    def __init__(self):
        self._matriz = []

    def cria_matriz(self):
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(randrange(2))
            self._matriz.append(linha)

        return self._matriz

    def __str__(self):
        for linha in self._matriz:
            print(linha)


x = Campo()
x.cria_matriz()
print(x)
