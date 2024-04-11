#Dupla = Diogo Xavier, José Kawan

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"Acelerando. Velocidade atual: {self.velocidade} km/h")
        else:
            print("Não é possível acelerar, o carro está desligado.")

meu_carro = Carro(marca="Toyota", modelo="Corolla", ano=2022, cor="prata")
print(f"Meu carro é um {meu_carro.marca} {meu_carro.modelo} {meu_carro.ano} de cor {meu_carro.cor}.")

meu_carro.ligar()
meu_carro.acelerar(20)
meu_carro.acelerar(30)
meu_carro.desligar()
meu_carro.acelerar(10)