class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            print("Não há notas disponíveis.")
            return None

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media is not None:
            if media >= 7:
                return "Aprovado"
            else:
                return "Reprovado"
        else:
            return "Não há notas disponíveis para verificar a aprovação."


estudante1 = Estudante(nome="João", idade=20, notas=[8, 7, 6, 9])

print(f"Média do estudante {estudante1.nome}: {estudante1.calcular_media()}")
print(f"Situação do estudante {estudante1.nome}: {estudante1.verificar_aprovacao()}")