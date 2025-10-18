from .Empilhavel import Empilhavel
from utils.excecoes.excecoesGerais import EstruturaCheiaError, EstruturaVaziaError
from typing import Any


class PilhaEstatica(Empilhavel):
    """
    Pilha estática implementada com lista fixa.

    Estamos estudando pilhas: LIFO (Last In, First Out).
    Esta classe usa programação orientada a objetos e docstrings em português
    para explicar a estrutura e seu funcionamento.
    """

    def __init__(self, capacidade: int = 10) -> None:
        """
        Inicializa a pilha estática com a capacidade informada.

        :param capacidade: número máximo de elementos que a pilha pode conter.
        """
        if capacidade <= 0:
            raise ValueError("capacidade deve ser > 0")
        self.capacidade: int = capacidade
        self.dados: list[Any] = [None] * capacidade
        self.topo: int = -1

    def empilhar(self, item: Any) -> None:
        """
        Adiciona um elemento ao topo da pilha.
        Lança EstruturaCheiaError se a pilha estiver cheia.
        """
        if self.estaCheia():
            raise EstruturaCheiaError("Pilha cheia: não há espaço para empilhar!")
        self.topo += 1
        self.dados[self.topo] = item

    def desempilhar(self) -> Any:
        """
        Remove e retorna o elemento do topo da pilha.
        Lança EstruturaVaziaError se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha vazia: não há dados para desempilhar!")
        item = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return item

    def espiar(self) -> Any:
        """
        Retorna o elemento do topo da pilha sem removê-lo.
        Lança EstruturaVaziaError se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha vazia!")
        return self.dados[self.topo]

    def atualizar(self, item: Any) -> None:
        """
        Atualiza o elemento do topo da pilha com um novo valor.
        Lança EstruturaVaziaError se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha vazia: não é possível atualizar!")
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
        if self.estaVazia():
            return "[]"
        linhas = []
        for i in range(self.topo, -1, -1):
            linhas.append(str(self.dados[i]))
        return "\n".join(linhas)
