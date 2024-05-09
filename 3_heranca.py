# Criando classes que herdam atributos e métodos de outra
class Pessoa:

    def andar(self):
        print('Estou andando.')
    
    def falar(self):
        print('Estou falando.')


class Vendedor(Pessoa):

    def vender(self):
        print('Estou vendendo.')
    


class Cliente(Pessoa):

    def comprar(self):
        print('Estou comprando.')


v1 = Vendedor()

v1.andar()
v1.vender()
v1.comprar() # Essa linha gera erro, pois 'v1' pertence à classe Vendedor, porém o método comprar é exclusivo da classe Cliente.
    
