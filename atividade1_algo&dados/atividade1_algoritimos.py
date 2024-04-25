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
    def __init__(self):
        self.id = None
        self.nome = str()

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        super().__init__()
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    @abstractmethod
    def getInformacoes(self):
        return f"Informações:\nModelo - {self.modelo}\nCor - {self.cor}\nPreco - {self.preco}\nCategoria - {self.categoria}\n"

    @abstractmethod
    def cadastrar(self, newModelo, newCor, newPreco, newCategoria):
        self.modelo = newModelo
        self.cor = newCor
        self.preco = newPreco
        self.categoria = newCategoria

    
class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def potenciaDaFonte(self):
        return str(self._potenciaDaFonte)
    
    @potenciaDaFonte.getter
    def potenciaDaFonte(self, newPotencia):
        self._potenciaDaFonte = newPotencia

    def getInformacoes(self):
        return super().getInformacoes() +"Potencia da Fonte - "+ self.potenciaDaFonte

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    @property
    def tempoDeBateria(self):
        return str(self.__tempoDeBateria)

    @tempoDeBateria.getter
    def tempoDeBateria(self, newTempoDeBateria):
        self.__tempoDeBateria = newTempoDeBateria

    def getInformacoes(self):
        return super().getInformacoes() +"Tempo de Bateria - " + self.tempoDeBateria
    
    

    