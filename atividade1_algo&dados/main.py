from atividade1_algoritimos import Desktop, Notebook, Categoria

produtos = []

def criar_notebook():
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    preco = input("Preco: ")
    bateria = input("Tempo de Bateria: ")
    novo_notebbok = Notebook(modelo, cor, preco, bateria)
    novo_notebbok.cadastrar('Notebook')
    return novo_notebbok

def criar_desktop():
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    preco = float(input("Preco: "))
    fonte = input("Potencia Fonte: ")
    novo_desktop = Desktop(modelo, cor, preco, fonte)
    novo_desktop.cadastrar('Desktop')
    return novo_desktop


def criar_produtos():
    novoProduto = int(input("Digite 1 se quiser cadastrar um Notebook\nDigite 2 se quiser cadastrar um Desktop: \n"))
    match novoProduto:
        case 1:
            produtos.append(criar_notebook())
        case 2:
            produtos.append(criar_desktop())
def lojinha():
    while True:
        menu = int(input("Digite - 1 se quiser cadastrar um produto\nDigite - 2 se quiser listar os produtos cadastrados\nDigite - 0 se quiser sair: \n"))
        match menu:
            case 1:
                criar_produtos()
            case 2:
                for indice, produto in enumerate(produtos):
                    print(f"{indice + 1} -  {produto.getInformacoes()}\n")
            case 0:
                print('Programa finalizado!')
                break

if __name__ == "__main__":
    lojinha()