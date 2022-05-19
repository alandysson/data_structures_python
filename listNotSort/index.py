from random import randint
from noh import *
from exception import MaiorQueLista


class ListaNaoOrdenada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        atual = self.head
        contador = 0
        while atual != None:
            contador = contador + 1
            atual = atual.getNext()
        return contador

    def search(self, item):
        atual = self.head  # atual == temp
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou

    def remove(self, item):
        atual = self.head
        anterior = None
        encontrou = False
        while not encontrou:  # percorre a lista
            if atual.getData() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()
            if anterior == None:
                self.head = atual.getNext()
            else:
                anterior.setNext(atual.getNext())

    def append(self, item):
        atual = self.head
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.getNext()
            if atual == None:
                addNovo = Noh(item)
                anterior.setNext(addNovo)

    def insert(self, posicao, item):
        atual = self.head
        anterior = None
        proximo = None
        count = 0
        addNovo = Noh(item)
        if posicao > self.size():
            raise MaiorQueLista(
                'Valor da posicao maior que o tamanho da lista')
        if posicao == 0:
            self.add(item)
        elif posicao == 1:
            anterior = atual
            atual = anterior.getNext()
            anterior.setNext(addNovo)
            addNovo.setNext(atual)
        else:
            while count < posicao - 1:
                anterior = atual
                atual = anterior.getNext()
                proximo = atual.getNext()
                count += 1

            atual.setNext(addNovo)
            addNovo.setNext(proximo)

    def pop(self):
        atual = self.head
        anterior = None
        proximo = None
        count = 0
        while count < self.size() - 1:
            anterior = atual
            atual = anterior.getNext()
            proximo = atual.getNext()
            count += 1
        anterior.setNext(proximo)
    # 2 - Verificar todos os item até chegar ao Nó vazio(ou um antes a ele), quando isso acontecer, apontar o anterior ao ultimo para o Nó vazio

    def push(self, item):
        return self.append(item)

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def show(self):
        return print(self.__repr__())


minha_lista = ListaNaoOrdenada()
for item in range(6):
    minha_lista.add(randint(1, 10))
# print(minha_lista)
# minha_lista.add(6)
minha_lista.insert(6, 11)
minha_lista.show()
