from abc import ABC, abstractmethod
from typing import Any

class Enfileiravel(ABC):
    """Interface (ABCs) para filas."""

    @abstractmethod
    def enfileirar(self, dado: Any) -> None:
        """C - enqueue"""
        raise NotImplementedError

    @abstractmethod
    def frente(self) -> Any:
        """R - front"""
        raise NotImplementedError

    @abstractmethod
    def atualizarInicio(self, dado: Any) -> None:
        """U - atualizar o elemento no início"""
        raise NotImplementedError

    @abstractmethod
    def atualizarFim(self, dado: Any) -> None:
        """U - atualizar o elemento no fim"""
        raise NotImplementedError

    @abstractmethod
    def desenfileirar(self) -> Any:
        """D - dequeue"""
        raise NotImplementedError

    @abstractmethod
    def estaCheia(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def estaVazia(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def imprimir(self) -> str:
        raise NotImplementedError