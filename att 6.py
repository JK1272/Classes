class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_nome(self, novo_nome):
        self.nome = novo_nome

    def definir_idade(self, nova_idade):
        self.idade = nova_idade

    def definir_altura(self, nova_altura):
        self.altura = nova_altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}. Prazer em conhecê-lo!"


pessoa1 = Pessoa(nome="Ana", idade=30, altura=1.65)

print("Nome:", pessoa1.obter_nome())
print("Idade:", pessoa1.obter_idade())
print("Altura:", pessoa1.obter_altura())

print(pessoa1.cumprimentar())