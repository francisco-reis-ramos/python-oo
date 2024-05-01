class Carros:
    
    def __init__(self, nome, montadora, ano):
        self.nome = nome
        self.montadora = montadora
        self.ano = ano

    def vender_carro (self):
        print(f'O carro {self.nome} foi vendido.')
    
carro1 = Carros('Astra', 'Chevrolet', 2004)
carro2 = Carros('Vectra', 'Chevrolet', 2003)
carro3 = Carros('Sentra', 'Nissan', 2013)

print(carro3.nome)
carro2.vender_carro()