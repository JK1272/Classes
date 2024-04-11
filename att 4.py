class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def atualizar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def calcular_preco_total(self, quantidade_desejada):
        if quantidade_desejada <= self.quantidade_estoque:
            preco_total = quantidade_desejada * self.preco
            return preco_total
        else:
            print("Quantidade desejada indisponível em estoque.")
            return None


produto1 = Produto(nome="Camiseta", preco=25.00, quantidade_estoque=50)

print(f"Nome do produto: {produto1.nome}")
print(f"Preço do produto: R${produto1.preco}")
print(f"Quantidade em estoque: {produto1.quantidade_estoque}")

produto1.atualizar_estoque(10)  
print(f"Nova quantidade em estoque: {produto1.quantidade_estoque}")

quantidade_desejada = 20
preco_total = produto1.calcular_preco_total(quantidade_desejada)
if preco_total is not None:
    print(f"Preço total para {quantidade_desejada} unidades: R${preco_total}")