class Veiculo: 
    def mover(self):
        print(" O Veiculo está se movendo")

class Carro(Veiculo):
    def mover(self):
        print("O Carro etá se movendo")

veiculos = [Carro()]
for veiculo in veiculos:
    veiculo.mover()        
