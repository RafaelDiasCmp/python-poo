class Pessoa:
    def __init__(self, nome=None, idade=None):
        self._nome = nome
        self._idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa('João', 35)
# print(p._nome, p._idade)

p = Pessoa.criar_de_data_nascimento(1990, 1, 1, 'João')
print(p._nome, p._idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))