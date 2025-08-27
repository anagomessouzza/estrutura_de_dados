from abc import ABC, abstractmethod

class Empilhavel(ABC):
    """
    Interface abstrata para estruturas de dados do tipo pilha.
    Esta classe define os métodos essenciais que qualquer implementação de pilha deve possuir,
    garantindo padronização e facilitando a manutenção e reutilização do código.

    Métodos abstratos principais:
        empilhar(item): Adiciona um elemento ao topo da pilha. (Create do CRUD)
        espiar(): Retorna o elemento do topo da pilha sem removê-lo.(Read do CRUD)
        atualizar(item): Atualiza o elemento do topo da pilha. (Update do CRUD)
        desempilhar(): Remove e retorna o elemento do topo da pilha. (Delete do CRUD)
        
    Métodos abstratos auxiliares:
        estaCheia() -> bool: Verifica se a pilha está cheia.
        estaVazia() -> bool: Verifica se a pilha está vazia.
        imprimir() -> str: Retorna uma representação em string dos elementos da pilha.
    """
    @abstractmethod
    def empilhar(self, item):
        pass
    
    @abstractmethod
    def desempilhar(self):
        pass
    
    @abstractmethod
    def espiar(self):
        pass
    
    @abstractmethod
    def atualizar(self, item):
        pass

    @abstractmethod
    def estaCheia(self) -> bool:
        pass

    @abstractmethod
    def estaVazia(self) -> bool:
        pass

    @abstractmethod
    def imprimir(self) -> str:
        pass