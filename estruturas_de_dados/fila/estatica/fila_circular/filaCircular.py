from __future__ import annotations
from typing import Any, Optional, List
from estruturas_de_dados.fila.estatica.fila.Enfileravel import Enfileiravel
from utils.excecoes.excecoesGerais import (
    EstruturaCheiaError,
    EstruturaVaziaError,
    CapacidadeInvalidaError,
)


class FilaCircular(Enfileiravel):
    """
    Fila estática circular implementada do zero (FIFO).

    Estudo:
    - Implementação com array fixo e uso de aritmética modular para avançar
      os ponteiros (início e fim), evitando deslocamentos ao desenfileirar.
    - Complexidades:
      * enfileirar: O(1)
      * desenfileirar: O(1)
      * frente/espiar: O(1)
    """

    def __init__(self, tamanho: int = 10) -> None:
        if tamanho <= 0:
            raise CapacidadeInvalidaError("Capacidade inválida: o tamanho deve ser maior que zero.")
        self.ponteiroInicio: int = 0
        self.ponteiroFim: int = -1
        self.quantidade: int = 0
        self.dados: List[Optional[Any]] = [None] * tamanho

    def enfileirar(self, dado: Any) -> None:
        """Insere um elemento no fim da fila (enqueue)."""
        if self.estaCheia():
            raise EstruturaCheiaError("Fila cheia: não é possível enfileirar.")
        self.ponteiroFim = self._avancar(self.ponteiroFim)
        self.dados[self.ponteiroFim] = dado
        self.quantidade += 1

    def desenfileirar(self) -> Optional[Any]:
        """Remove e retorna o elemento da frente (dequeue)."""
        if self.estaVazia():
            raise EstruturaVaziaError("Fila vazia: não é possível desenfileirar.")
        dadoInicio = self.dados[self.ponteiroInicio]
        self.dados[self.ponteiroInicio] = None
        self.ponteiroInicio = self._avancar(self.ponteiroInicio)
        self.quantidade -= 1
        return dadoInicio

    def frente(self) -> Optional[Any]:
        """Retorna (sem remover) o elemento da frente da fila."""
        if self.estaVazia():
            raise EstruturaVaziaError("Fila vazia: não há elemento na frente.")
        return self.dados[self.ponteiroInicio]

    def atualizarInicio(self, dado: Any) -> None:
        """Atualiza o elemento que está na frente da fila."""
        if self.estaVazia():
            raise EstruturaVaziaError("Fila vazia: não é possível atualizar o início.")
        self.dados[self.ponteiroInicio] = dado

    def atualizarFim(self, dado: Any) -> None:
        """Atualiza o elemento que está no fim da fila."""
        if self.estaVazia():
            raise EstruturaVaziaError("Fila vazia: não é possível atualizar o fim.")
        self.dados[self.ponteiroFim] = dado

    def estaCheia(self) -> bool:
        """Retorna True se a fila estiver cheia."""
        return self.quantidade == len(self.dados)

    def estaVazia(self) -> bool:
        """Retorna True se a fila estiver vazia."""
        return self.quantidade == 0

    def imprimir(self) -> str:
        """Retorna a representação em string da fila na ordem da frente ao fim."""
        if self.estaVazia():
            return "[]"
        elementos: List[str] = []
        ponteiroAux = self.ponteiroInicio
        for _ in range(self.quantidade):
            elementos.append(repr(self.dados[ponteiroAux]))
            ponteiroAux = self._avancar(ponteiroAux)
        return "[" + ",".join(elementos) + "]"

    def _avancar(self, ponteiro: int) -> int:
        """Avança o ponteiro de forma circular usando aritmética modular."""
        return (ponteiro + 1) % len(self.dados)