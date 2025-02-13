class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print('Removendo a instância da classe...')

    def falar(self):
        print('🐶 Au au au au au...')

def criar_cachorro():
    c1 = Cachorro('Rex', 'marrom', False)
    print(c1.nome)

c = Cachorro('Totó', 'branco')
c.falar()

print('Olá mundo')

del c

        