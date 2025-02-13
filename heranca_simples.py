class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def buzinar(self):
        print('🔔 Trim...trim...')

    def ligar_motor(self):
        print('🔑 Ligando motor...')
        print('🚗 Motor ligado!')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'🚛 Caminhão carregado!' if self.carregado else 'Não carregado'}")



moto = Motocicleta('preta', 'ABC-1234', 2)

carro = Carro('branco', 'XYZ-9876', 4)

caminhao = Caminhao('vermelho', 'DEF-4567', 8, True)


print(moto)
print(carro)
print(caminhao)