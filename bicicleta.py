class Bicicleta:  
    def __init__(self, cor, modelo, ano, valor):  
        self.cor = cor  
        self.modelo = modelo  
        self.ano = ano  
        self.valor = valor 

    def buzinar(self):
        print('🔔 Trim...trim...')

    def parar(self):
        print('🛑 Parando bicicleta...')
        print('✅ Bicicleta parada!')

    def correr(self):
        print('🚴💨 VRUUUUUMMMM')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

# Criando o objeto
b1 = Bicicleta('vermelha', 'caloi', 2022, 600)

# Chamando métodos
b1.correr()
b1.buzinar()
b1.parar()

# Exibir atributos da bicicleta de forma formatada
print(b1)  

# Exibir atributos individualmente
print(b1.cor, b1.modelo, b1.ano, b1.valor)
