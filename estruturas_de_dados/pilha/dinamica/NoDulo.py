from __future__ import annotations
from typing import Any, Optional


class NoDuplo:
    """
    Nó duplo 
    Objetivo de estudo:
    - Nó para listas/pilhas duplamente encadeadas.
    - Removemos a parametrização por TypeVar para simplificar o uso em Python
      (tipos são tratados como Any em tempo de execução).
    - Documenta em português o que está sendo estudado: referências forward/back,
      operações O(1) para manipulação de ponteiros.

    Atributos:
    - dado: valor armazenado no nó (qualquer tipo).
    - proximo: referência para o próximo nó ou None.
    - anterior: referência para o nó anterior ou None.
    """

    def __init__(
        self,
        dado: Any = None,
        proximo: Optional[NoDuplo] = None,
        anterior: Optional[NoDuplo] = None,
    ) -> None:
        """
        Inicializa o nó duplo.

        :param dado: valor a armazenar no nó (qualquer tipo).
        :param proximo: referência para o próximo nó (ou None).
        :param anterior: referência para o nó anterior (ou None).
        """
        self.dado: Any = dado
        self.proximo: Optional[NoDuplo] = proximo
        self.anterior: Optional[NoDuplo] = anterior

    def get_dado(self) -> Any:
        """Retorna o valor armazenado no nó."""
        return self.dado

    def set_dado(self, novo: Any) -> None:
        """Define/atualiza o valor armazenado no nó."""
        self.dado = novo

    def get_proximo(self) -> Optional[NoDuplo]:
        """Retorna referência ao próximo nó (ou None)."""
        return self.proximo

    def set_proximo(self, no: Optional[NoDuplo]) -> None:
        """Define a referência para o próximo nó."""
        self.proximo = no

    def get_anterior(self) -> Optional[NoDuplo]:
        """Retorna referência ao nó anterior (ou None)."""
        return self.anterior

    def set_anterior(self, no: Optional[NoDuplo]) -> None:
        """Define a referência para o nó anterior."""
        self.anterior = no

    def desvincular(self) -> None:
        """Remove referências para facilitar coleta de lixo ao remover o nó."""
        self.proximo = None
        self.anterior = None

    def __repr__(self) -> str:
        """Representação curta para depuração."""
        return f"NoDuplo({self.dado!r})"