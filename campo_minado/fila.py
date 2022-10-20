class Fila:
    def __init__(self):
        self._dados = [None]
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def first(self):
        if self.is_empty():
            raise ('A Fila está vazia')
        return self._dados[self._inicio]

    def dequeue(self):
        if self.is_empty():
            raise ('A Fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def enqueue(self, e):  # - - x x x -
        if self._tamanho == len(self._dados):
            self._aumenta_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1

    # novo_tamanho precisar ser >= len(self)
    def _aumenta_tamanho(self, novo_tamanho):
        dados_antigos = self._dados  # keep track of existing list
        self._dados = [None] * novo_tamanho  # allocate list with new capacity
        posicao = self._inicio
        for k in range(self._tamanho):  # only consider existing elements
            # intentionally shift indices
            self._dados[k] = dados_antigos[posicao]
        # use dados_antigos size as modulus
        posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0


if __name__ == "__main__":
    x = Fila()
    x.enqueue(10)
    x.enqueue(2)
    print(x.first())
