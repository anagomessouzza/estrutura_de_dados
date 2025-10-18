from __future__ import annotations
from typing import Any, List, Optional

from estruturas_de_dados.lista.estatica.lista.Listavel import Listavel
from utils.excecoes.excecoesGerais import (
    EstruturaCheiaError,
    EstruturaVaziaError,
    CapacidadeInvalidaError,
    IndiceInvalidoError,
)


class ListaEstaticaCircular(Listavel):
    """
    Lista estática circular (implementação de Listavel).

    Estudo:
    - Implementação com array fixo e aritmética modular para mapear índices lógicos
      (0..n-1) para posições físicas no array.
    - Permite inserção, remoção e acesso por posição lógica sem deslocar todo o array
      em sentido absoluto (usamos ponteiroInicio e ponteiroFim e fazemos deslocamentos
      locais conforme necessário).
    - Complexidades dependem da operação:
      * anexar (inserir no fim): O(1)
      * selecionar (acesso por índice): O(1)
      * inserir/apagar em posição arbitrária: O(n) no pior caso (deslocamentos)
    - Todo método documentado em português para fins didáticos.
    """

    def __init__(self, tamanho: int = 10) -> None:
        if tamanho <= 0:
            raise CapacidadeInvalidaError("Capacidade inválida: o tamanho deve ser maior que zero.")
        self._dados: List[Optional[Any]] = [None] * tamanho
        self._ponteiroInicio: int = 0
        self._ponteiroFim: int = -1
        self._quantidade: int = 0

    # --- helpers de endereçamento/aritmética modular ---
    def _mapeamento(self, logica: int) -> int:
        """Converte posição lógica (0..quantidade-1) para índice físico no array."""
        return (logica + self._ponteiroInicio) % len(self._dados)

    def _avancar(self, ponteiro: int) -> int:
        return (ponteiro + 1) % len(self._dados)

    def _retroceder(self, ponteiro: int) -> int:
        return (ponteiro - 1 + len(self._dados)) % len(self._dados)

    # --- estado ---
    def estaCheia(self) -> bool:
        return self._quantidade == len(self._dados)

    def estaVazia(self) -> bool:
        return self._quantidade == 0

    # --- representação ---
    def imprimir(self) -> str:
        if self.estaVazia():
            return "[]"
        elementos: List[str] = []
        idx = self._ponteiroInicio
        for _ in range(self._quantidade):
            elementos.append(repr(self._dados[idx]))
            idx = self._avancar(idx)
        return "[" + ",".join(elementos) + "]"

    # --- operações principais ---
    def anexar(self, dado: Any) -> None:
        """Insere no final (equivalente a inserir na posição lógica quantidade)."""
        if self.estaCheia():
            raise EstruturaCheiaError("Lista cheia: não é possível anexar.")
        self._ponteiroFim = self._avancar(self._ponteiroFim)
        self._dados[self._ponteiroFim] = dado
        self._quantidade += 1
        if self._quantidade == 1:
            self._ponteiroInicio = self._ponteiroFim

    def selecionarTodos(self) -> List[Any]:
        """Retorna uma lista Python com todos os elementos, na ordem lógica."""
        if self.estaVazia():
            raise EstruturaVaziaError("Lista vazia: não há elementos para selecionar.")
        resultado: List[Any] = []
        idx = self._ponteiroInicio
        for _ in range(self._quantidade):
            resultado.append(self._dados[idx])
            idx = self._avancar(idx)
        return resultado

    def selecionar(self, posicao: int) -> Optional[Any]:
        """Retorna o elemento na posição lógica informada (0..quantidade-1)."""
        if self.estaVazia():
            raise EstruturaVaziaError("Lista vazia: não é possível selecionar.")
        if posicao < 0 or posicao >= self._quantidade:
            raise IndiceInvalidoError(f"Índice inválido: {posicao}.")
        posFisica = self._mapeamento(posicao)
        return self._dados[posFisica]

    def atualizar(self, posicao: int, novoDado: Any) -> None:
        """Substitui o elemento na posição lógica informada por novoDado."""
        if self.estaVazia():
            raise EstruturaVaziaError("Lista vazia: não é possível atualizar.")
        if posicao < 0 or posicao >= self._quantidade:
            raise IndiceInvalidoError(f"Índice inválido: {posicao}.")
        posFisica = self._mapeamento(posicao)
        self._dados[posFisica] = novoDado

    def inserir(self, posicao: int, dado: Any) -> None:
        """
        Insere 'dado' na posição lógica 'posicao' (0..quantidade).
        Caso posicao == quantidade, equivale a anexar.
        Desloca elementos necessários para abrir espaço.
        """
        if self.estaCheia():
            raise EstruturaCheiaError("Lista cheia: não é possível inserir.")
        if posicao < 0 or posicao > self._quantidade:
            raise IndiceInvalidoError(f"Índice inválido para inserção: {posicao}.")

        # inserir no fim (caso simples)
        if posicao == self._quantidade:
            self.anexar(dado)
            return

        # abertura de espaço: mover elementos [posicao..quantidade-1] um passo à direita
        novoFim = self._avancar(self._ponteiroFim)  # posição física livre para o novo fim
        src = self._ponteiroFim
        dst = novoFim
        passos = self._quantidade - posicao  # quantos elementos mover
        for _ in range(passos):
            self._dados[dst] = self._dados[src]
            dst = self._retroceder(dst)
            src = self._retroceder(src)

        posFisica = self._mapeamento(posicao)
        self._dados[posFisica] = dado
        self._ponteiroFim = novoFim
        self._quantidade += 1
        if self._quantidade == 1:
            self._ponteiroInicio = self._ponteiroFim

    def apagar(self, posicao: int) -> Optional[Any]:
        """
        Remove e retorna o elemento na posição lógica posicao.
        Desloca elementos à esquerda para preencher o buraco.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Lista vazia: não é possível apagar.")
        if posicao < 0 or posicao >= self._quantidade:
            raise IndiceInvalidoError(f"Índice inválido para remoção: {posicao}.")

        posFisica = self._mapeamento(posicao)
        valor = self._dados[posFisica]

        # mover elementos [posicao+1 .. quantidade-1] um passo à esquerda
        src = self._avancar(posFisica)
        dst = posFisica
        passos = self._quantidade - posicao - 1
        for _ in range(passos):
            self._dados[dst] = self._dados[src]
            dst = self._avancar(dst)
            src = self._avancar(src)

        # limpar antiga posição do fim e atualizar ponteiroFim
        self._dados[self._ponteiroFim] = None
        self._ponteiroFim = self._retroceder(self._ponteiroFim)
        self._quantidade -= 1

        if self._quantidade == 0:
            # resetar para estado inicial consistênte
            self._ponteiroInicio = 0
            self._ponteiroFim = -1

        return valor