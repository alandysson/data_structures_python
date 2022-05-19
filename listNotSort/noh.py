class Noh:
    def __init__(self, valor_inicial):
        self._dados = valor_inicial
        self._proximo = None

    def getData(self):
        return self._dados

    def getNext(self):
        return self._proximo

    def setData(self, novo_valor):
        self._dados = novo_valor

    def setNext(self, novo_proximo):
        self._proximo = novo_proximo

    def __repr__(self):
        return '{} -> {}'.format(self._dados, self._proximo)
