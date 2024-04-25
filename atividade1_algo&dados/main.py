from atividade1_algoritimos import Desktop, Produto

produtos = []

def criar_produtos():
    novoProduto = int(input("Digite 1 se quiser cadastrar um Notebook\nDigite 2 se quiser cadastrar um Desktop: "))
    match novoProduto:
        case 1:
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            preco = float(input("Preco: "))
            categoria = input("Categoria: ")
            fonte = input("Potencia Fonte: ")

def lojinha():
    menu = int(input("Digite - 1 se quiser cadastrar um produto\nDigite - 2 se quiser listar os produtos cadastrados: "))
    match menu:
        case 1:
            


if __name__ == "__main__":
