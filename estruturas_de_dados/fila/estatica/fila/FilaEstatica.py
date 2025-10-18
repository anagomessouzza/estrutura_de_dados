from typing import Any, List, Optional
import sys

from estruturas_de_dados.fila.estatica.fila.Enfileravel import Enfileiravel


class FilaEstatica(Enfileiravel):
    """Fila estática (não circular) traduzida do exemplo Java."""

    def __init__(self, tamanho: int = 10) -> None:
        self.ponteiroInicio: int = 0
        self.ponteiroFim: int = -1
        self.dados: List[Optional[Any]] = [None] * tamanho

    def enfileirar(self, dado: Any) -> None:
        if not self.estaCheia():
            self.ponteiroFim += 1
            self.dados[self.ponteiroFim] = dado
        else:
            print("Fila Cheia!", file=sys.stderr)

    def desenfileirar(self) -> Optional[Any]:
        dadoInicio: Optional[Any] = None
        if not self.estaVazia():
            dadoInicio = self.dados[self.ponteiroInicio]
            self.dados[self.ponteiroInicio] = None
            self.ponteiroInicio += 1
        else:
            print("Fila Vazia!", file=sys.stderr)
        return dadoInicio

    def frente(self) -> Optional[Any]:
        dadoInicio: Optional[Any] = None
        if not self.estaVazia():
            dadoInicio = self.dados[self.ponteiroInicio]
        else:
            print("Fila Vazia!", file=sys.stderr)
        return dadoInicio

    def atualizarInicio(self, dado: Any) -> None:
        if not self.estaVazia():
            self.dados[self.ponteiroInicio] = dado
        else:
            print("Fila Vazia!", file=sys.stderr)

    def atualizarFim(self, dado: Any) -> None:
        if not self.estaVazia():
            self.dados[self.ponteiroFim] = dado
        else:
            print("Fila Vazia!", file=sys.stderr)

    def estaCheia(self) -> bool:
        return self.ponteiroFim == len(self.dados) - 1

    def estaVazia(self) -> bool:
        return self.ponteiroInicio == self.ponteiroFim + 1

    def imprimir(self) -> str:
        if self.estaVazia():
            return "[]"
        partes: List[str] = []
        for i in range(self.ponteiroInicio, self.ponteiroFim + 1):
            partes.append(str(self.dados[i]))
        return "[" + ", ".join(partes) + "]"