from utils import *

def menu():
  return print(
    """
    --- Cadastrador de Veiculos ---
                           
    1 - Adicionar novo Veiculo
    2 - Remover veiculo
    3 - Consultar veiculo cadastrado

    4 - Encerrar programa
    --------------------------------
    """
  )

verify = 0
operacao = UtilsVeiculo()
while verify != 4:
  menu()
  verify = int(input(":"))
  print()
  if verify == 1:
    adiciona = operacao.cadastrarVeiculo()
    if adiciona != -1:
      operacao.adicionaVeiculoNaLista(adiciona)
  elif verify == 2:
    placa = input("Digite a placa(ex: AAAA000): ")
    print()
    operacao.removeVeiculoDaLista(placa)
  elif verify == 3:
    placa = input("Digite a placa(ex: AAAA000): ")
    print()
    operacao.mostraVeiculo(placa)
  elif verify == 5:
    operacao.todosVeiculos()
    