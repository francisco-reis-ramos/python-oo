# Criando a classe Pessoas
class Pessoas:

    possui_olho = True  # Atributo da classe Pessoas
    possui_boca = True  # Atributo da classe Pessoas
    possui_pernas = True # Atributo da classe Pessoas
    
    def __init__(self, nome, idade, cpf): # Atributos da classe 
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self): # Método logar_sistema
        print(f'{self.retorna_nome()} está logando no sistema')

    def logout_sistema(self): # Método logout_sistema
        print(f'{self.retorna_nome()} está saindo do sistema')

    # Criando um método de classe.
    # Os atributos da classe podem estar dentro do método ou fora dele. São inseridos dentro quando deseja-se criar o atributo com a condição estabelecida pelo método.
    @classmethod
    def amputado(cls):
        cls.possui_pernas = False
        return None

    # Criando um método estático.
    # Ao contrário do método de classe, esse não pode alterar atributos da classe. Não consegue acessar ou modificar qualquer atributo da classe, é apenas um método utilitário.
    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False


# Criando instancias da classe Pessoas
p1 = Pessoas('Alfredo', 74, '98785454468')
p2 = Pessoas('Jamil', 27, '47635897724')

# Saídas do Programa
print(p1.nome)
p1.logar_sistema()

# Perceba abaixo que o valor retornado para 'print(Pessoas.possui_pernas)' varia a partir do momento em que o método amputado() é chamado.
# Isso demonstra o funcionamento de um atributo que esteja condicionado a um método. 
print(Pessoas.possui_pernas)
Pessoas.amputado()
print(Pessoas.possui_pernas)

# Método estático
print(Pessoas.e_adulto(25))


