from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Optional


class Listavel(ABC):
    """
    Interface (ABC) para listas estáticas/dinâmicas.

    Objetivo de estudo:
    - Implementar listas do zero para aprender operações básicas: inserção, remoção,
      seleção e atualização por posição lógica.
    - Esta interface define o contrato mínimo que implementações concretas
      (listas estáticas, listas ligadas etc.) devem seguir.

    Notas pedagógicas:
    - Posição lógica refere-se ao índice do elemento na visão do usuário (0..n-1).
    - Complexidades dependem da implementação concreta (por exemplo, lista estática:
      anexar O(1) amortizado, inserir/apagar O(n) por deslocamentos; lista ligada:
      inserir/apagar O(1) se tiver referência ao nó).
    - Use docstrings nas implementações para explicar comportamentos e complexidades.
    """

    @abstractmethod
    def anexar(self, dado: Any) -> None:
        """Anexa (insere ao final) o novo dado na lista."""
        raise NotImplementedError

    @abstractmethod
    def inserir(self, posicao: int, dado: Any) -> None:
        """Insere o novo dado na posição lógica informada (0..tamanho)."""
        raise NotImplementedError

    @abstractmethod
    def selecionar(self, posicao: int) -> Optional[Any]:
        """Retorna o elemento que está na posição lógica informada ou None se inválida."""
        raise NotImplementedError

    @abstractmethod
    def selecionarTodos(self) -> List[Any]:
        """Retorna todos os elementos da lista como uma lista Python."""
        raise NotImplementedError

    @abstractmethod
    def atualizar(self, posicao: int, novoDado: Any) -> None:
        """Substitui o elemento da posição lógica informada pelo novo dado."""
        raise NotImplementedError

    @abstractmethod
    def apagar(self, posicao: int) -> Optional[Any]:
        """Remove e retorna o elemento da posição lógica informada, ou None se inválida."""
        raise NotImplementedError

    # métodos auxiliares
    @abstractmethod
    def estaCheia(self) -> bool:
        """Retorna True se a lista atingiu sua capacidade (útil para implementação estática)."""
        raise NotImplementedError

    @abstractmethod
    def estaVazia(self) -> bool:
        """Retorna True se a lista não contém elementos."""
        raise NotImplementedError

    @abstractmethod
    def imprimir(self) -> str:
        """Retorna uma representação em string dos elementos (para depuração/visualização)."""
        raise NotImplementedError