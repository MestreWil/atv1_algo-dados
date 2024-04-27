from abc import ABC, abstractmethod

"""
Construir código necessário em Python para implementar o seguinte projeto: Uma classe Categoria que possui os atributos id e nome. 
Uma classe abstrata chamada de Produto que contém os atributos/propriedades: modelo, cor, preço e categoria. 
Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos. 
Esta classe também possui um método abstrato cadastrar().
O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto. 
A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
Esta classe reimplementa o método getInformacoes() herdado de Produto.
A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. 
Esta classe reimplementa o método getInformacoes() herdado de Produto. 
Construa getters e setters para os atributos que não forem públicos. Todas as classes devem ter um método construtor.
Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.
Crie um repositório no github, faça commit e push para este repositório e entreque aqui apenas o link do repositório.
"""

class Categoria:
    def __init__(self, nome):
        self.id = None
        self.nome = nome
        
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, newnome):
        self.nome = newnome
        
    def __str__(self):
        return f'{self.nome}'

class Produto(ABC):
    def __init__(self, modelo, cor, preco):
        super().__init__()
        self.modelo = str(modelo)
        self.cor = str(cor)
        self.preco = float(preco)
        self.categoria = None

    @abstractmethod
    def getInformacoes(self):
        return f"Informações:\nModelo - {self.modelo}\nCor - {self.cor}\nPreco - {self.preco}\nCategoria - {self.categoria}\n"

    @abstractmethod
    def cadastrar(self):
        pass
    
class Desktop(Produto):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def potenciaDaFonte(self):
        return str(self._potenciaDaFonte)
    
    @potenciaDaFonte.getter
    def potenciaDaFonte(self, newPotencia):
        self._potenciaDaFonte = newPotencia

    def getInformacoes(self):
        return super().getInformacoes() + f"Potencia da Fonte - {self._potenciaDaFonte}" 
    
    def cadastrar(self, categoria):
        self.categoria = categoria
    

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    @property
    def tempoDeBateria(self):
        return str(self.__tempoDeBateria)

    @tempoDeBateria.getter
    def tempoDeBateria(self, newTempoDeBateria):
        self.__tempoDeBateria = newTempoDeBateria

    def getInformacoes(self):
        return super().getInformacoes() + f"Tempo de Bateria - {self.__tempoDeBateria}"
    def cadastrar(self, categoria):
        self.categoria = categoria
    
    