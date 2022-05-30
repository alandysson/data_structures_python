from hashtable import HashTable
auditorio = HashTable(2)


class Menu:
    def __init__(self):
        self._matricula = None
        self._nome = None

    def menu(self):
        print("1- Adicionar: \n2- Pesquisar: ")
        menu = int(input("opcao: "))
        if menu == 1:
            self.criar()
            self.mensagem()
        elif menu == 2:
            senha = int(input("Senha do aluno: "))
            self.buscar(senha)

    def criar(self):
        self._nome = input('Nome do aluno completo: ')
        self._matricula = int(input('Matricula: '))
        auditorio.put(self._matricula, self._nome)

    def buscar(self, chave):
        aluno = auditorio[chave]
        if(aluno[0] != None):
            print('O aluno {} esta na cadeira {}'.format(
                aluno[0], aluno[1]))
        else:
            print(
                'Não foi possivel encontrar esse aluno. Senha errada ou aluno não está no evento')

    def mensagem(self):
        if auditorio[self._matricula][0] != None:
            return print('O aluno {} foi cadastrado, sua senha eh {} e sua cadeira eh a {}'.format(
                self._nome, self._matricula, auditorio[self._matricula][1]))

        print('Auditório lotado')


verify = None
menu = Menu()
while verify != 'N':
    menu.menu()
    verify = input('Deseja contiunar (s/n)? ').upper()
