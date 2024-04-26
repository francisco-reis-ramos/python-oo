# Criando a classe Pessoas
class Pessoas:

    possui_olho = True  # Atributo da classe Pessoas
    possui_boca = True  # Atributo da classe Pessoas
    
    def __init__(self, nome, idade, cpf): # Atributos da classe 
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def logar_sistema(self): # Método logar_sistema
        print(f'{self.nome} está logando no sistema')

    def logout_sistema(self): # Método logout_sistema
        print(f'{self.nome} está saindo do sistema')

# Criando instancias da classe Pessoas
p1 = Pessoas('Alfredo', 74, '98785454468')
p2 = Pessoas('Jamil', 27, '47635897724')

# Saídas do Programa
print(p1.nome)
p1.logar_sistema()
p1.logout_sistema()

