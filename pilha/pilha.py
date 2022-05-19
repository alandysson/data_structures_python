from xml.etree.ElementTree import PI
from pilhaVazia import *
from pilhaCheia import *


class PilhaArray:

    def __init__(self, TAMANHO_MAXIMO):
        self._TAMANHO_MAXIMO = TAMANHO_MAXIMO
        self._pilha = []

    def __len__(self):
        return len(self._pilha)

    def size(self):
        return self.__len__()

    def is_empty(self):
        return len(self._pilha) == 0

    def is_full(self):
        return self.size() == self._TAMANHO_MAXIMO

    def push(self, e):
        if self.is_full():
            raise PilhaCheia('A pilha está cheia')
        self._pilha.append(e)

    def top(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha[-1]

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha.pop()

    def removeTodos(self, tamanhoPilha):
        if tamanhoPilha == 0:
            return self.is_empty()
        else:
            self.pop()
            return 1 + self.removeTodos(tamanhoPilha - 1)

    def inverteDados(self):
        novaLista = []
        while not self.is_empty():
            novaLista.append(self.pop())
        return novaLista

    def __str__(self):
        return "{}".format(self._pilha)


if __name__ == "__main__":
    from random import randint

    pilha = PilhaArray(7)
    for i in range(6):
        pilha.push(randint(1, 10))

   #  pilha.removeTodos(pilha.size())
    print(pilha)
    novaLista = pilha.inverteDados()
    print(novaLista)
