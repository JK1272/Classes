class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        raise NotImplementedError("Método 'emitir_som' não implementado para esta espécie de animal.")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Espécie: {self.especie}")


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, especie="Cachorro")

    def emitir_som(self):
        print("Au au!")


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, especie="Gato")

    def emitir_som(self):
        print("Miau!")


meu_cachorro = Cachorro(nome="Rex", idade=3)
meu_gato = Gato(nome="Whiskers", idade=5)

print("Informações sobre o cachorro:")
meu_cachorro.mostrar_informacoes()
meu_cachorro.emitir_som()

print("\nInformações sobre o gato:")
meu_gato.mostrar_informacoes()
meu_gato.emitir_som()