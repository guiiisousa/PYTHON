def adicionar_produto(carrinho, produto):
    carrinho.append(produto)

def remover_produto(carrinho, produto):
    if produto in carrinho:
        carrinho.remove(produto)
    else:
        print(f"O produto {produto} não está no carrinho.") 
        
def exibir_carrinho(carrinho):
    if carrinho:
        print("Produtos no carrinho:")
        for produto in carrinho:
            print(f"- {produto}")
    else:
        print("O carrinho está vazio.")

def Verificar_produto(carrinho, produto):
    if produto in carrinho:
        print(f"O produto {produto} está no carrinho.")
    else:
        print(f"O produto {produto} não está no carrinho.")