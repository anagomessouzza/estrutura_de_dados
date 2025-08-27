from Empilhavel import Empilhavel
from excecoes.Excecoes import EstaCheiaException, EstaVaziaException

class PilhaEstatica(Empilhavel):
    def __init__(self, capacidade=10):
        """
        Inicializa a pilha estática com a capacidade informada.
        """
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.topo = -1

    def empilhar(self, item):
        """
        Adiciona um elemento ao topo da pilha.
        Lança EstaCheiaException se a pilha estiver cheia.
        """
        if self.estaCheia():
            raise EstaCheiaException("Pilha cheia: não há dados para empilhar!")
        self.topo += 1
        self.dados[self.topo] = item

    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha.
        Lança EstaVaziaException se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstaVaziaException("Pilha vazia: não há dados para desempilhar!")
        item = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return item

    def espiar(self):
        """
        Retorna o elemento do topo da pilha sem removê-lo.
        Lança EstaVaziaException se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstaVaziaException("Pilha vazia!")
        return self.dados[self.topo]

    def atualizar(self, item):
        """
        Atualiza o elemento do topo da pilha com um novo valor.
        Lança EstaVaziaException se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstaVaziaException("Pilha vazia: não é possível atualizar!")
        self.dados[self.topo] = item

    def estaCheia(self) -> bool:
        """
        Verifica se a pilha está cheia.
        :return: True se cheia, False caso contrário.
        """
        return self.topo == self.capacidade - 1

    def estaVazia(self) -> bool:
        """
        Verifica se a pilha está vazia.
        :return: True se vazia, False caso contrário.
        """
        return self.topo == -1

    def imprimir(self) -> str:
        """
        Retorna uma representação em string dos elementos da pilha, do topo até a base.
        """
        resultado = "["
        for i in range(self.topo, -1, -1):
            resultado += str(self.dados[i])
            if i != 0:
                resultado += ","
        resultado += "]"
        return resultado
