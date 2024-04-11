class Pedido:
    def __init__(self):
        self.itens = {}
        self.total = 0
        self.status = "Pendente"

    def adicionar_item(self, nome_item, preco_item):
        if nome_item in self.itens:
            self.itens[nome_item] += 1
        else:
            self.itens[nome_item] = 1
        self.total += preco_item

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status


pedido1 = Pedido()

pedido1.adicionar_item(nome_item="Hamburguer", preco_item=10)
pedido1.adicionar_item(nome_item="Batata Frita", preco_item=5)
pedido1.adicionar_item(nome_item="Refrigerante", preco_item=3)

print("Itens do pedido:", pedido1.itens)
print("Total a ser pago:", pedido1.calcular_total())
print("Status do pedido:", pedido1.status)

pedido1.alterar_status("Em preparo")
print("Novo status do pedido:", pedido1.status)