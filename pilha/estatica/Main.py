from pilha.estatica.PilhaEstatica import PilhaEstatica
from excecoes.Excecoes import EstaCheiaException, EstaVaziaException

class MenuPilhaEstatica:
    def __init__(self, capacidade=10):
        self.pilha = PilhaEstatica(capacidade)

    def exibir_menu(self):
        print("\nMenu:")
        print("1 - Empilhar")
        print("2 - Desempilhar")
        print("3 - Atualizar topo")
        print("4 - Espiar topo")
        print("5 - Imprimir pilha")
        print("0 - Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                item = input("Digite o valor para empilhar: ")
                try:
                    self.pilha.empilhar(item)
                    print("Empilhado com sucesso!")
                except EstaCheiaException as e:
                    print(e)
            elif opcao == "2":
                try:
                    removido = self.pilha.desempilhar()
                    print(f"Desempilhado: {removido}")
                except EstaVaziaException as e:
                    print(e)
            elif opcao == "3":
                novo_item = input("Digite o novo valor para o topo: ")
                try:
                    self.pilha.atualizar(novo_item)
                    print("Topo atualizado com sucesso!")
                except EstaVaziaException as e:
                    print(e)
            elif opcao == "4":
                try:
                    topo = self.pilha.espiar()
                    print(f"Topo da pilha: {topo}")
                except EstaVaziaException as e:
                    print(e)
            elif opcao == "5":
                print("Pilha:", self.pilha.imprimir())
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

        print("\nPilha final:", self.pilha.imprimir())

if __name__ == "__main__":
    menu = MenuPilhaEstatica()
    menu.executar()