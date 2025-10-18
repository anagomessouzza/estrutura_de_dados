from typing import Optional

"""
Módulo de exceções customizadas para as estruturas de dados do projeto.

Estamos estudando estruturas de dados do zero: filas, pilhas, listas, etc.
Este módulo agrupa exceções reutilizáveis para sinalizar condições típicas
(dados vazios, capacidade inválida, índices fora do intervalo, etc.).

Uso:
    from utils.excecoes.Excecoes import EstruturaVaziaError, EstruturaCheiaError

Explicação (didática):
    - Ao implementar operações como desempilhar ou desenfileirar, é comum
      encontrar condições de erro específicas da estrutura (por ex. tentar
      remover um elemento de uma estrutura vazia). Exceções específicas tornam
      o código mais claro e facilitam o tratamento de erros nos testes e na
      lógica superior.
"""

class EstruturaDadosError(Exception):
    """Erro base para todas as exceções relacionadas às estruturas de dados.

    Aceita uma mensagem customizada; caso não seja fornecida, usa uma mensagem
    genérica descritiva.
    """

    DEFAULT_MESSAGE = "Erro em estrutura de dados."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class EstruturaVaziaError(EstruturaDadosError):
    """Lançada quando uma operação exige elementos mas a estrutura está vazia.

    Exemplo: desenfileirar de uma fila vazia, desempilhar de uma pilha vazia.
    """

    DEFAULT_MESSAGE = "Estrutura vazia: não foi possível realizar a operação."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class EstruturaCheiaError(EstruturaDadosError):
    """Lançada quando não é possível inserir porque a estrutura atingiu a capacidade."""

    DEFAULT_MESSAGE = "Estrutura cheia: não é possível inserir novos elementos."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class CapacidadeInvalidaError(EstruturaDadosError):
    """Lançada quando um parâmetro de capacidade é inválido (<= 0)."""

    DEFAULT_MESSAGE = "Capacidade inválida: o tamanho deve ser maior que zero."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class IndiceInvalidoError(EstruturaDadosError):
    """Lançada quando um índice informado está fora do intervalo válido."""

    DEFAULT_MESSAGE = "Índice inválido: fora do intervalo permitido."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class ElementoNaoEncontradoError(EstruturaDadosError):
    """Lançada quando uma operação espera localizar um elemento e não o encontra."""

    DEFAULT_MESSAGE = "Elemento não encontrado na estrutura."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)


class OperacaoInvalidaError(EstruturaDadosError):
    """Lançada quando uma operação não faz sentido no contexto atual."""

    DEFAULT_MESSAGE = "Operação inválida para o estado atual da estrutura."

    def __init__(self, mensagem: Optional[str] = None) -> None:
        super().__init__(mensagem or self.DEFAULT_MESSAGE)