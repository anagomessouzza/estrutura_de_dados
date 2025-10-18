from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class DuplamenteEnfileiravel(ABC):
    """
    Interface (ABC) para filas de dupla terminação (deque).

    Objetivo de estudo:
    - Entender e implementar uma deque (double-ended queue), que permite
      operações em ambas as extremidades (início/frente e fim/trás).
    - Fornecer um contrato claro para implementações estáticas/dinâmicas.

    Notas pedagógicas:
    - Use esta interface para implementar Deques estáticos (arrays circulares)
      ou dinâmicos (listas ligadas, duas pilhas, etc.).
    - Cada método documenta a operação esperada e suas responsabilidades.
    """

    @abstractmethod
    def enfileirarInicio(self, dado: Any) -> None:
        """Insere 'dado' no início da estrutura (equivalente a push_front)."""

    @abstractmethod
    def enfileirarFim(self, dado: Any) -> None:
        """Insere 'dado' no fim da estrutura (equivalente a push_back)."""

    @abstractmethod
    def desenfileirarInicio(self) -> Optional[Any]:
        """Remove e retorna o elemento do início (front). Retorna None ou lança erro se vazio."""

    @abstractmethod
    def desenfileirarFim(self) -> Optional[Any]:
        """Remove e retorna o elemento do fim (rear). Retorna None ou lança erro se vazio."""

    @abstractmethod
    def frente(self) -> Optional[Any]:
        """Retorna (sem remover) o elemento da frente (front/peek)."""

    @abstractmethod
    def tras(self) -> Optional[Any]:
        """Retorna (sem remover) o elemento de trás (rear/peek)."""

    @abstractmethod
    def atualizarInicio(self, dado: Any) -> None:
        """Atualiza o elemento que está na frente com 'dado'."""

    @abstractmethod
    def atualizarFim(self, dado: Any) -> None:
        """Atualiza o elemento que está no fim com 'dado'."""

    @abstractmethod
    def estaCheia(self) -> bool:
        """Retorna True se a estrutura estiver cheia (útil para implementações estáticas)."""

    @abstractmethod
    def estaVazia(self) -> bool:
        """Retorna True se a estrutura estiver vazia."""

    @abstractmethod
    def imprimirDeFrentePraTras(self) -> str:
        """Retorna uma representação em string dos elementos da frente para trás."""

    @abstractmethod
    def imprimirDeTrasPraFrente(self) -> str:
        """Retorna uma representação em string dos elementos de trás para trás"""