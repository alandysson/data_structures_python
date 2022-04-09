class Veiculo:
    def __init__(self, placa, marca, modelo, ano, cod_proprietario):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cod_proprietario = cod_proprietario

    def imprimeVeiculo(self):
        return ("Placa: {} \nMarca: {} \nModelo: {} \nAno: {} \nCodigo do Proprietario: {} \n".format(self._placa, self._marca, self._modelo, self._ano, self._cod_proprietario))

    def imprimeFinalPlaca(self):
        return self._placa[3:]

    def ultimoNumero(self):
        return self._placa[-1]
        
    def placa(self):
      return self._placa
