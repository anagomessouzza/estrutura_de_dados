from typing import Any
import sys
from estruturas_de_dados.fila.estatica.fila.Enfileravel import Enfileiravel
from estruturas_de_dados.pilha.estatica.pilha.Empilhavel import Empilhavel
from estruturas_de_dados.pilha.estatica.pilha.Pilha import PilhaEstatica


class FilaComPilhas(Enfileiravel):
    """
    Implementação de fila usando duas pilhas estáticas.
    
    Objetivo de estudo:
    - Entender como aplicar duas pilhas para simular o comportamento FIFO de uma fila.
    - Manter a fila orientada a objetos e bem documentada, explicando a lógica.

    Estratégia:
    - Mantemos os elementos na pilha p1 de modo que o topo de p1 represente a frente (front) da fila.
      Para enfileirar, transferimos todos os elementos de p1 para p2, empilhamos o novo elemento em p1
      (que está vazia) e então devolvemos os elementos de p2 para p1. Assim a ordem FIFO é preservada.
    - Desenfileirar é simplesmente desempilhar de p1 (topo = frente).
    Complexidades:
    - enfileirar: O(n) no pior caso (n = número de elementos) devido às transferências entre pilhas.
    - desenfileirar: O(1).
    """

    def __init__(self, tamanho: int = 10) -> None:
        """
        Inicializa as duas pilhas que compõem a fila.
        """
        self.p1: Empilhavel = PilhaEstatica(tamanho)
        self.p2: Empilhavel = PilhaEstatica(tamanho)

    def enfileirar(self, dado: Any) -> None:
        """
        Enfileira um elemento mantendo a ordem FIFO.
        Se a fila estiver cheia, escreve mensagem no stderr (seguindo o estilo dos exemplos).
        """
        if not self.estaCheia():
            # mover p1 -> p2
            while not self.p1.estaVazia():
                self.p2.empilhar(self.p1.desempilhar())

            # empilhar o novo elemento em p1 (agora vazia)
            self.p1.empilhar(dado)

            # mover de volta p2 -> p1
            while not self.p2.estaVazia():
                self.p1.empilhar(self.p2.desempilhar())
        else:
            print("Fila Cheia!", file=sys.stderr)

    def desenfileirar(self) -> Any:
        """
        Remove e retorna o elemento da frente (topo de p1).
        """
        if not self.estaVazia():
            return self.p1.desempilhar()
        print("Fila Vazia!", file=sys.stderr)
        return None

    def frente(self) -> Any:
        """
        Retorna (sem remover) o elemento da frente.
        """
        if not self.estaVazia():
            return self.p1.espiar()
        print("Fila Vazia!", file=sys.stderr)
        return None

    def atualizarInicio(self, dado: Any) -> None:
        """
        Atualiza o elemento na frente da fila (topo de p1).
        """
        if not self.estaVazia():
            # Empilhavel define atualizar() que substitui o topo
            self.p1.atualizar(dado)
        else:
            print("Fila Vazia!", file=sys.stderr)

    def atualizarFim(self, dado: Any) -> None:
        """
        Atualiza o elemento no fim (rear) da fila.
        Estratégia: esvaziar p1 em p2; o último desempilhado corresponde ao rear original;
        substituímos esse elemento e então devolvemos tudo para p1.
        """
        if self.estaVazia():
            print("Fila Vazia!", file=sys.stderr)
            return

        # transferir todos os elementos de p1 para p2
        while not self.p1.estaVazia():
            self.p2.empilhar(self.p1.desempilhar())

        # p2.top agora é o antigo rear; removemos e substituímos por 'dado'
        _ = self.p2.desempilhar()  # descarta o antigo rear
        self.p2.empilhar(dado)     # empilha o novo rear

        # devolver elementos para p1, reaproveitando a ordem
        while not self.p2.estaVazia():
            self.p1.empilhar(self.p2.desempilhar())

    def estaCheia(self) -> bool:
        """
        Determina se a fila está cheia. Basta checar p1 (mesma capacidade aplicada a ambas).
        """
        return self.p1.estaCheia()

    def estaVazia(self) -> bool:
        """
        Verifica se a fila está vazia.
        """
        return self.p1.estaVazia()

    def imprimir(self) -> str:
        """
        Retorna a representação em string da fila delegando para p1.
        """
        return self.p1.imprimir()