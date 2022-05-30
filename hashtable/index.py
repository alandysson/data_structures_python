class HashTable:
    def __init__(self):
        self._slots = [None] * self._tamanho
        self._valores = [None] * self._tamanho

    def hashfunction(self, chave, tamanho):
        return chave % tamanho

    def rehash(self, oldhash, tamanho):
        return (oldhash+1) % tamanho

    def put(self, chave, valor):
        valor_hash = self.hashfunction(chave, len(self._slots))
        pos_inicial = valor_hash
        if self._slots[valor_hash] == None:
            self._slots[valor_hash] = chave
            self._valores[valor_hash] = valor
        else:
            if self._slots[valor_hash] == chave:
                self._valores[valor_hash] = valor  # replace
            else:
                proximo_slot = self.rehash(valor_hash, len(self._slots))
            while self._slots[proximo_slot] != None and \
                    self._slots[proximo_slot] != chave and \
                    proximo_slot != pos_inicial:
                proximo_slot = self.rehash(proximo_slot, len(self._slots))
            if self._slots[proximo_slot] == None:
                self._slots[proximo_slot] = chave
                self._valores[proximo_slot] = valor
            elif chave == self._slots[proximo_slot]:
                self._valores[proximo_slot] = valor  # replace

    def get(self, chave):
        slot_inicial = self.hashfunction(chave, len(self._slots))
        valor = None
        parar = False
        encontrou = False
        posicao = slot_inicial
        while self._slots[posicao] != None and not encontrou and not parar:
            if self._slots[posicao] == chave:
                encontrou = True
                valor = self._valores[posicao]
            else:
                posicao = self.rehash(posicao, len(self._slots))
                if posicao == slot_inicial:
                    parar = True
        return valor

    def __getitem__(self, chave):
        return self.get(chave)

    def __setitem__(self, chave, valor):
        self.put(chave, valor)


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H._slots)
    #[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    print(H._valores)
    #['bird', 'goat', 'pig', 'chicken', 'dog', 'lion','tiger', None, None, 'cow', 'cat']
    print(H.get(54))  # 'tiger'
    H[20] = 'duck'
    H[66] = 'fly'
    print(H[20])  # 'duck'
    # ['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', 'fly', None, 'cow', 'cat']
    print(H._valores)
    print(H[99])  # None
