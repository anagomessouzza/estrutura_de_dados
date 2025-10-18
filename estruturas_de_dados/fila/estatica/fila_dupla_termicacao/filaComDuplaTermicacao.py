from __future__ import annotations
from typing import Any, List, Optional
from utils.excecoes.excecoesGerais import (
    EstruturaCheiaError,
    EstruturaVaziaError,
    CapacidadeInvalidaError,
)
from enfileiravelDuplaTerminacao import DuplamenteEnfileiravel


class FilaComDuplaTermicacao(DuplamenteEnfileiravel):
    """
    Fila de dupla terminação estática (deque) implementada com array circular.

    Estudamos deque (double-ended queue): permite operações em ambas extremidades.
    Esta implementação é estática (capacidade fixa) e usa aritmética modular
    para avançar/retroceder índices sem mover elementos.
    """

    def __init__(self, tamanho: int = 10) -> None:
        if tamanho <= 0:
            raise CapacidadeInvalidaError("Capacidade inválida: deve ser > 0.")
        self._dados: List[Optional[Any]] = [None] * tamanho
        self._inicio: int = 0   # índice do elemento da frente (front)
        self._fim: int = -1     # índice do elemento do rear (último válido)
        self._quantidade: int = 0

    def enfileirarInicio(self, dado: Any) -> None:
        if self.estaCheia():
            raise EstruturaCheiaError("Deque cheio: não é possível inserir no início.")
        # mover início para trás (circular) e colocar dado
        self._inicio = (self._inicio - 1) % len(self._dados)
        self._dados[self._inicio] = dado
        self._quantidade += 1
        if self._quantidade == 1:
            # primeiro elemento: fim coincide com início
            self._fim = self._inicio

    def enfileirarFim(self, dado: Any) -> None:
        if self.estaCheia():
            raise EstruturaCheiaError("Deque cheio: não é possível inserir no fim.")
        self._fim = (self._fim + 1) % len(self._dados)
        self._dados[self._fim] = dado
        self._quantidade += 1
        if self._quantidade == 1:
            self._inicio = self._fim

    def desenfileirarInicio(self) -> Optional[Any]:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não é possível remover do início.")
        valor = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._quantidade -= 1
        if self._quantidade == 0:
            # reset índices para estado inicial
            self._inicio = 0
            self._fim = -1
        return valor

    def desenfileirarFim(self) -> Optional[Any]:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não é possível remover do fim.")
        valor = self._dados[self._fim]
        self._dados[self._fim] = None
        self._fim = (self._fim - 1) % len(self._dados)
        self._quantidade -= 1
        if self._quantidade == 0:
            self._inicio = 0
            self._fim = -1
        return valor

    def frente(self) -> Optional[Any]:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não há elemento na frente.")
        return self._dados[self._inicio]

    def tras(self) -> Optional[Any]:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não há elemento no fim.")
        return self._dados[self._fim]

    def atualizarInicio(self, dado: Any) -> None:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não é possível atualizar início.")
        self._dados[self._inicio] = dado

    def atualizarFim(self, dado: Any) -> None:
        if self.estaVazia():
            raise EstruturaVaziaError("Deque vazio: não é possível atualizar fim.")
        self._dados[self._fim] = dado

    def estaCheia(self) -> bool:
        return self._quantidade == len(self._dados)

    def estaVazia(self) -> bool:
        return self._quantidade == 0

    def imprimirDeFrentePraTras(self) -> str:
        if self.estaVazia():
            return "[]"
        elementos: List[str] = []
        idx = self._inicio
        for _ in range(self._quantidade):
            elementos.append(repr(self._dados[idx]))
            idx = (idx + 1) % len(self._dados)
        return "[" + ",".join(elementos) + "]"

    def imprimirDeTrasPraFrente(self) -> str:
        if self.estaVazia():
            return "[]"
        elementos: List[str] = []
        idx = self._fim
        for _ in range(self._quantidade):
            elementos.append(repr(self._dados[idx]))
            idx = (idx - 1) % len(self._dados)
        return "[" + ",".join(elementos) + "]"