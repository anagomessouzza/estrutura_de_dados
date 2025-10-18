from __future__ import annotations
from typing import Any, Optional
from estruturas_de_dados.pilha.dinamica.NoDulo import NoDuplo
from estruturas_de_dados.pilha.estatica.pilha.Empilhavel import Empilhavel
from utils.excecoes.excecoesGerais import EstruturaCheiaError, EstruturaVaziaError


class PilhaDinamicaGenerica(Empilhavel):
    """
    Pilha dinâmica usando nós duplamente encadeados..

    Observações:
    - Removemos TypeVar/Generic para compatibilizar com NoDuplo (que não é genérico).
    - Em Python as anotações são para auxílio estático; em runtime aceitamos Any como elemento.
    - Operações: empilhar/desempilhar/espiar/atualizar/estaCheia/estaVazia/imprimir.
    """

    def __init__(self, tamanho: int = 10) -> None:
        """
        Inicializa a pilha dinâmica com capacidade 'tamanho' (padrão 10).

        :param tamanho: capacidade máxima lógica da pilha.
        """
        if tamanho <= 0:
            raise ValueError("capacidade deve ser > 0")
        self.quantidade: int = 0
        self.tamanho: int = tamanho
        self.ponteiroTopo: Optional[NoDuplo] = None

    def empilhar(self, dado: Any) -> None:
        """
        Empilha 'dado' no topo da pilha.
        Lança EstruturaCheiaError se a pilha já atingiu a capacidade.
        """
        if self.estaCheia():
            raise EstruturaCheiaError("Pilha Cheia!")
        no_novo = NoDuplo(dado)
        # anterior do novo é o antigo topo (ponteiroTopo pode ser None)
        no_novo.set_anterior(self.ponteiroTopo)
        no_novo.set_proximo(None)
        if not self.estaVazia():
            # antigo topo passa a apontar para o novo como próximo
            assert self.ponteiroTopo is not None
            self.ponteiroTopo.set_proximo(no_novo)
        self.ponteiroTopo = no_novo
        self.quantidade += 1

    def desempilhar(self) -> Any:
        """
        Desempilha e retorna o elemento do topo.
        Lança EstruturaVaziaError se a pilha estiver vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha Vazia!")
        assert self.ponteiroTopo is not None
        dado = self.ponteiroTopo.get_dado()
        # mover topo para o anterior
        novo_topo = self.ponteiroTopo.get_anterior()
        # desvincular nó removido
        self.ponteiroTopo.desvincular()
        self.ponteiroTopo = novo_topo
        self.quantidade -= 1
        if not self.estaVazia():
            assert self.ponteiroTopo is not None
            self.ponteiroTopo.set_proximo(None)
        return dado

    def espiar(self) -> Any:
        """
        Retorna o elemento do topo sem removê-lo.
        Lança EstruturaVaziaError se vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha Vazia!")
        assert self.ponteiroTopo is not None
        return self.ponteiroTopo.get_dado()

    def atualizar(self, novoDado: Any) -> None:
        """
        Atualiza o valor do topo da pilha para 'novoDado'.
        Lança EstruturaVaziaError se vazia.
        """
        if self.estaVazia():
            raise EstruturaVaziaError("Pilha Vazia!")
        assert self.ponteiroTopo is not None
        self.ponteiroTopo.set_dado(novoDado)

    def estaCheia(self) -> bool:
        """Retorna True se a pilha atingiu a capacidade máxima."""
        return self.quantidade == self.tamanho

    def estaVazia(self) -> bool:
        """Retorna True se a pilha não possui elementos."""
        return self.quantidade == 0

    def imprimir(self) -> str:
        """
        Retorna uma representação da pilha como string.
        Formato: [elem_base,...,elem_topo] — o topo será o último elemento exibido.
        """
        if self.estaVazia():
            return "[]"
        elementos = []
        ponteiro = self.ponteiroTopo
        # iterar do topo para a base coletando elementos
        for _ in range(self.quantidade):
            assert ponteiro is not None
            elementos.append(repr(ponteiro.get_dado()))
            ponteiro = ponteiro.get_anterior()
        # mostrar da base para o topo (topo último)
        elementos_reversos = list(reversed(elementos))
        return "[" + ",".join(elementos_reversos) + "]"