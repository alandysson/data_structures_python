from veiculo import *

class UtilsVeiculo:
  def __init__(self):
    self._listaVeiculos = []

  def cadastrarVeiculo(self):
    placa = input("Digite a placa(ex:AAAA000): ")
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo: ")
    ano = input("Digite o ano: ")
    cod_proprietario = int(input("Digite o codigo do proprietario: "))

    verifica = [placa, marca, modelo, ano]

    # o retorno -1 é um erro nos dados de cadastramento
    if len(placa) != 7:
      print("Placa preenchida incorretamente")
      return -1 
    else:
      for i in placa[4:]:
        if ord(i) < 48 or ord(i) > 57:
          print("Placa preenchida incorretamente")
          return -1 
    
    if len(ano) < 4:
      print("Ano preenchido incorretamente")
      return -1 
    
    for item in range(len(verifica)):
      if len(verifica[item]) == 0:
        print("O {}º campo não foi preenchido corretamente".format(item))
        return -1

    return Veiculo(placa, marca, modelo, ano, cod_proprietario)
    
  def adicionaVeiculoNaLista(self, veiculo):
    self._listaVeiculos.append(veiculo)

  def removeVeiculoDaLista(self, placa):
    count = 0
    if len(self._listaVeiculos) == 0:
      return print("Não há veiculos registrado")
    for veiculoAtual in self._listaVeiculos:
      count += 1
      if placa == veiculoAtual.placa():
        self._listaVeiculos.pop(count - 1)
        print("Registro Removido!")
        return self._listaVeiculos
    
  def mostraVeiculo(self, placa):
    if len(placa) == 1:
      if ord(placa) >= 48 or ord(placa) <= 57:
        for veiculoAtual in self._listaVeiculos:
          if placa == veiculoAtual.ultimoNumero(): 
            print(veiculoAtual.imprimeVeiculo())
        return  
    for veiculoAtual in self._listaVeiculos:
      if placa == veiculoAtual.placa(): 
        return print(veiculoAtual.imprimeVeiculo())
      
    return print("Nao ha veiculo cadastrado com essa placa")

  def todosVeiculos(self):
    for veiculoAtual in self._listaVeiculos:
      print(veiculoAtual.imprimeVeiculo())
    
    